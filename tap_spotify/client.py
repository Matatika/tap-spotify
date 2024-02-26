"""REST client handling, including SpotifyStream base class."""

from typing import Iterable, Optional
from urllib.parse import ParseResult, parse_qsl

from memoization import cached
from singer_sdk.streams import RESTStream

from tap_spotify.auth import SpotifyAuthenticator
from tap_spotify.pagination import BodyLinkPaginator


class SpotifyStream(RESTStream):
    """Spotify stream class."""

    url_base = "https://api.spotify.com/v1"
    records_jsonpath = "$.items[*]"
    chunk_size = None

    @property
    @cached
    def authenticator(self):
        return SpotifyAuthenticator.create_for_stream(self)

    def get_new_paginator(self):
        return BodyLinkPaginator()

    def get_url_params(self, context, next_page_token: Optional[ParseResult]):
        params = super().get_url_params(context, next_page_token)
        return dict(parse_qsl(next_page_token.query)) if next_page_token else params

    def chunk_records(self, records: Iterable[dict]):
        if not self.chunk_size:
            return [records]

        chunk = []

        for i, record in enumerate(records):
            if i and not i % self.chunk_size:
                yield list(chunk)
                chunk.clear()

            chunk.append(record)

        if chunk:
            yield list(chunk)
