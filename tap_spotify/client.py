"""REST client handling, including SpotifyStream base class."""

from datetime import datetime
from typing import Optional
from urllib.parse import ParseResult, parse_qsl

from memoization import cached
from singer_sdk.exceptions import FatalAPIError, RetriableAPIError
from singer_sdk.streams import RESTStream

from tap_spotify.auth import SpotifyAuthenticator
from tap_spotify.pagination import BodyLinkPaginator


class SpotifyStream(RESTStream):
    """Spotify stream class."""

    url_base = "https://api.spotify.com/v1"
    records_jsonpath = "$.items[*]"

    @property
    @cached
    def authenticator(self):
        authenticator = SpotifyAuthenticator.create_for_stream(self)

        access_token = self.config.get("access_token")

        if access_token:
            authenticator.access_token = access_token
            # indicate user-supplied access token
            authenticator.last_refreshed = datetime.now()

        return authenticator

    def get_new_paginator(self):
        return BodyLinkPaginator()

    def get_url_params(self, context, next_page_token: Optional[ParseResult]):
        params = super().get_url_params(context, next_page_token)
        return dict(parse_qsl(next_page_token.query)) if next_page_token else params

    def _request(self, prepared_request, context):
        # reapply authenticator if retrying with oauth credentials
        if not self.authenticator.last_refreshed:
            prepared_request.prepare_auth(self.authenticator)

        self.logger.info(prepared_request.headers)
        return super()._request(prepared_request, context)

    def validate_response(self, response):
        try:
            super().validate_response(response)
        except FatalAPIError as e:
            if (
                response.status_code == 401
                # attempted with user-supplied access token
                and not self.authenticator.expires_in
                # oauth credentials provided
                and self.authenticator.client_id
                and self.authenticator.client_secret
                and self.authenticator.refresh_token
            ):
                # retry with oauth credentials
                self.authenticator.last_refreshed = None

                msg = self.response_error_message(response)
                raise RetriableAPIError(msg, response)

            raise e
