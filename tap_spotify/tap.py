"""Spotify tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_spotify.streams import (
    SpotifyStream,
    UsersStream,
    GroupsStream,
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    UsersStream,
    GroupsStream,
]


class TapSpotify(Tap):
    """Spotify tap class."""

    name = "tap-spotify"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            description="App client ID",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            description="App client secret",
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=True,
            description="Refresh token",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
