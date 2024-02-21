"""Tests standard tap features using the built-in SDK tests library."""


from singer_sdk.testing import get_tap_test_class

from tap_spotify.tap import TapSpotify

SAMPLE_CONFIG = {}


# Run standard built-in tap tests from the SDK:
TestTapSpotify = get_tap_test_class(
    tap_class=TapSpotify,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
