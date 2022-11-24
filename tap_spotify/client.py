"""REST client handling, including SpotifyStream base class."""

from typing import Any, Dict, Optional
from urllib.parse import parse_qsl, urlsplit

import requests
from memoization import cached
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

from tap_spotify.auth import SpotifyAuthenticator


class SpotifyStream(RESTStream):
    """Spotify stream class."""

    url_base = "https://api.spotify.com/v1"

    records_jsonpath = "$.items[*]"
    next_page_token_jsonpath = "$.next"

    @property
    @cached
    def authenticator(self) -> SpotifyAuthenticator:
        """Return a new authenticator object."""
        return SpotifyAuthenticator.create_for_stream(self)

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        all_matches = extract_jsonpath(self.next_page_token_jsonpath, response.json())
        return next(iter(all_matches), None)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        return dict(parse_qsl(urlsplit(next_page_token).query))
