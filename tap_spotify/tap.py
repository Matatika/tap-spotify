"""Spotify tap class."""

from singer_sdk import Tap
from singer_sdk import typing as th
from typing_extensions import override

from tap_spotify import streams

STREAM_TYPES = [
    streams.UserTopTracksShortTermStream,
    streams.UserTopTracksMediumTermStream,
    streams.UserTopTracksLongTermStream,
    streams.UserTopArtistsShortTermStream,
    streams.UserTopArtistsMediumTermStream,
    streams.UserTopArtistsLongTermStream,
    streams.GlobalTopTracksDailyStream,
    streams.GlobalTopTracksWeeklyStream,
    streams.GlobalViralTracksDailyStream,
    streams.UserSavedTracksStream,
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
            secret=True,
            description="App client secret",
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=True,
            secret=True,
            description="Refresh token",
        ),
    ).to_dict()

    @override
    def discover_streams(self):
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapSpotify.cli()
