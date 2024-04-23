"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_spotify.tap import TapSpotify, streams

SAMPLE_CONFIG = {}


# Run standard built-in tap tests from the SDK:
TestTapSpotify = get_tap_test_class(
    tap_class=TapSpotify,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        ignore_no_records_for_streams=[
            streams.UserTopTracksShortTermStream.__name__,
            streams.UserTopTracksMediumTermStream.__name__,
            streams.UserTopTracksLongTermStream.__name__,
            streams.UserTopArtistsShortTermStream.__name__,
            streams.UserTopArtistsMediumTermStream.__name__,
            streams.UserTopArtistsLongTermStream.__name__,
        ]
    ),
)
