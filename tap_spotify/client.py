"""REST client handling, including SpotifyStream base class."""

from typing import Any, Dict, Optional
from urllib.parse import ParseResult, parse_qsl

from memoization import cached
from singer_sdk.streams import RESTStream

from tap_spotify.auth import SpotifyAuthenticator
from tap_spotify.pagination import BodyLinkPaginator


class SpotifyStream(RESTStream):
    """Spotify stream class."""

    url_base = "https://api.spotify.com/v1"
    records_jsonpath = "$.items[*]"

    @property
    @cached
    def authenticator(self) -> SpotifyAuthenticator:
        """Return a new authenticator object."""
        return SpotifyAuthenticator.create_for_stream(self)

    def get_new_paginator(self):
        return BodyLinkPaginator()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[ParseResult]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        return dict(parse_qsl(next_page_token.query)) if next_page_token else {}
