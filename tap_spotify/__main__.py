"""Spotify entry point.

Copyright (c) 2026 Meltano.
"""

from __future__ import annotations

from tap_spotify.tap import TapSpotify

TapSpotify.cli()
