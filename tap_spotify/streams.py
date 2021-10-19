"""Stream type classes for tap-spotify."""

from itertools import count
from typing import Any, Dict, Optional

from singer_sdk.streams.rest import RESTStream

from tap_spotify.client import SpotifyStream
from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.track import TrackObject
from tap_spotify.schemas.utils.indexed import Indexed


class _IndexedStream(RESTStream):
    """Define an indexed stream."""

    index = 1

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """Apply index to stream"""
        row["index"] = self.index
        self.index += 1
        return row


class UserTopTracksShortTermStream(_IndexedStream, SpotifyStream):
    """Define user top tracks short-term stream."""

    name = "user_top_tracks_st_stream"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = Indexed(ArtistObject()).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "short_term"
        return params


class UserTopTracksMediumTermStream(_IndexedStream, SpotifyStream):
    """Define user top tracks medium-term stream."""

    name = "user_top_tracks_mt_stream"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = Indexed(ArtistObject()).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "medium_term"
        return params


class UserTopTracksLongTermStream(_IndexedStream, SpotifyStream):
    """Define user top tracks long-term stream."""

    name = "user_top_tracks_lt_stream"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = Indexed(ArtistObject()).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "long_term"
        return params


class UserTopArtistsShortTermStream(_IndexedStream, SpotifyStream):
    """Define user top artists short-term stream."""

    name = "user_top_artists_st_stream"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = Indexed(ArtistObject()).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "short_term"
        return params


class UserTopArtistsMediumTermStream(_IndexedStream, SpotifyStream):
    """Define user top artists medium-term stream."""

    name = "user_top_artists_mt_stream"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = Indexed(ArtistObject()).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "medium_term"
        return params


class UserTopArtistsLongTermStream(_IndexedStream, SpotifyStream):
    """Define user top artists long-term stream."""

    name = "user_top_artists_lt_stream"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = Indexed(ArtistObject()).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "long_term"
        return params


class _PlaylistTracksStream(_IndexedStream, SpotifyStream):
    """Define playlist tracks stream."""

    records_jsonpath = "$.tracks.items[*].track"
    primary_keys = ["id"]
    schema = Indexed(TrackObject()).schema


class GlobalTopTracksDailyStream(_PlaylistTracksStream):
    """Define global top tracks daily stream."""

    name = "global_top_tracks_daily_stream"
    path = "/playlists/37i9dQZEVXbMDoHDwVN2tF"


class GlobalTopTracksWeeklyStream(_PlaylistTracksStream):
    """Define global top tracks weekly stream."""

    name = "global_top_tracks_weekly_stream"
    path = "/playlists/37i9dQZEVXbNG2KDcFcKOF"


class GlobalViralTracksDailyStream(_PlaylistTracksStream):
    """Define global viral tracks daily stream."""

    name = "global_viral_tracks_daily_stream"
    path = "/playlists/37i9dQZEVXbLiRSasKsNU9"
