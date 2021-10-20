"""Stream type classes for tap-spotify."""

from datetime import datetime
from typing import Any, Dict, Optional

from singer_sdk.streams.rest import RESTStream

from tap_spotify.client import SpotifyStream
from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.track import TrackObject
from tap_spotify.schemas.utils.rank import Rank
from tap_spotify.schemas.utils.synced_at import SyncedAt


class _RankStream(RESTStream):
    """Define a rank stream."""

    rank = 1

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """Apply rank integer to stream"""
        row = super().post_process(row, context)
        row["rank"] = self.rank
        self.rank += 1
        return row


class _SyncedAtStream(RESTStream):
    """Define a synced at stream."""

    synced_at = datetime.utcnow()

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """Apply synced at datetime to stream"""
        row = super().post_process(row, context)
        row["synced_at"] = self.synced_at
        return row


class UserTopTracksShortTermStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top tracks short-term stream."""

    name = "user_top_tracks_st_stream"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = Rank(SyncedAt(TrackObject())).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "short_term"
        return params


class UserTopTracksMediumTermStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top tracks medium-term stream."""

    name = "user_top_tracks_mt_stream"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = Rank(SyncedAt(TrackObject())).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "medium_term"
        return params


class UserTopTracksLongTermStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top tracks long-term stream."""

    name = "user_top_tracks_lt_stream"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = Rank(SyncedAt(TrackObject())).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "long_term"
        return params


class UserTopArtistsShortTermStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top artists short-term stream."""

    name = "user_top_artists_st_stream"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = Rank(SyncedAt(ArtistObject())).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "short_term"
        return params


class UserTopArtistsMediumTermStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top artists medium-term stream."""

    name = "user_top_artists_mt_stream"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = Rank(SyncedAt(ArtistObject())).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "medium_term"
        return params


class UserTopArtistsLongTermStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top artists long-term stream."""

    name = "user_top_artists_lt_stream"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = Rank(SyncedAt(ArtistObject())).schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "long_term"
        return params


class _PlaylistTracksStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define playlist tracks stream."""

    records_jsonpath = "$.tracks.items[*].track"
    primary_keys = ["id"]
    schema = Rank(SyncedAt(TrackObject())).schema


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
