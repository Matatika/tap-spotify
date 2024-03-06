"""REST client handling, including SpotifyStream base class."""

from __future__ import annotations

from functools import cached_property
from typing import Iterable
from urllib.parse import parse_qsl

from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_spotify.auth import SpotifyAuthenticator
from tap_spotify.pagination import BodyLinkPaginator


class SpotifyStream(RESTStream):
    """Spotify stream class."""

    url_base = "https://api.spotify.com/v1"
    records_jsonpath = "$.items[*]"
    chunk_size: int | None

    @cached_property
    @override
    def authenticator(self):
        return SpotifyAuthenticator.create_for_stream(self)

    @override
    def get_new_paginator(self):
        return BodyLinkPaginator()

    @override
    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        return dict(parse_qsl(next_page_token.query)) if next_page_token else params

    def chunk_records(self, records: Iterable[dict]):  # noqa: D102
        if not self.chunk_size:
            return [records]

        chunk: list[dict] = []

        for i, record in enumerate(records):
            if i and not i % self.chunk_size:
                yield list(chunk)
                chunk.clear()

            chunk.append(record)

        if chunk:
            yield list(chunk)
