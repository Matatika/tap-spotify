"""Pagination classes for tap-spotify.

Copyright (c) 2026 Meltano.
"""

from singer_sdk.pagination import BaseHATEOASPaginator
from typing_extensions import override


class BodyLinkPaginator(BaseHATEOASPaginator):
    """Body `next` link paginator."""

    @override
    def get_next_url(self, response):
        data: dict = response.json()
        return data.get("next")
