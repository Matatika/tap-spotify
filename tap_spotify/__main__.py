"""Spotify entry point."""

from __future__ import annotations

from tap_spotify.tap import TapSpotify

TapSpotify.cli()
