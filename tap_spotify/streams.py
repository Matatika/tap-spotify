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


class _UserTopItemsStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top items stream."""

    time_range = "medium_term"
    limit = 49

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = self.time_range
        params["limit"] = self.limit
        return params


class _UserTopItemsShortTermStream(_UserTopItemsStream):
    """Define user top items short-term stream."""

    time_range = "short_term"


class _UserTopItemsLongTermStream(_UserTopItemsStream):
    """Define user top items long-term stream."""

    time_range = "long_term"


class _UserTopTracksStream(_UserTopItemsStream):
    """Define user top tracks stream."""

    path = "/me/top/tracks"
    schema = TrackObject.extend_with(Rank, SyncedAt).schema


class _UserTopArtistsStream(_UserTopItemsStream):
    """Define user top artists stream."""

    path = "/me/top/artists"
    schema = ArtistObject.extend_with(Rank, SyncedAt).schema


class UserTopTracksShortTermStream(
    _UserTopItemsShortTermStream,
    _UserTopTracksStream,
):
    """Define user top tracks short-term stream."""

    name = "user_top_tracks_st_stream"
    primary_keys = ["rank", "synced_at"]


class UserTopTracksMediumTermStream(_UserTopTracksStream):
    """Define user top tracks medium-term stream."""

    name = "user_top_tracks_mt_stream"
    primary_keys = ["rank", "synced_at"]


class UserTopTracksLongTermStream(
    _UserTopItemsLongTermStream,
    _UserTopTracksStream,
):
    """Define user top tracks long-term stream."""

    name = "user_top_tracks_lt_stream"
    primary_keys = ["rank", "synced_at"]


class UserTopArtistsShortTermStream(
    _UserTopItemsShortTermStream,
    _UserTopArtistsStream,
):
    """Define user top artists short-term stream."""

    name = "user_top_artists_st_stream"
    primary_keys = ["rank", "synced_at"]


class UserTopArtistsMediumTermStream(_UserTopArtistsStream):
    """Define user top artists medium-term stream."""

    name = "user_top_artists_mt_stream"
    primary_keys = ["rank", "synced_at"]


class UserTopArtistsLongTermStream(
    _UserTopItemsLongTermStream,
    _UserTopArtistsStream,
):
    """Define user top artists long-term stream."""

    name = "user_top_artists_lt_stream"
    primary_keys = ["rank", "synced_at"]


class _PlaylistTracksStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define playlist tracks stream."""

    records_jsonpath = "$.tracks.items[*].track"
    schema = TrackObject.extend_with(Rank, SyncedAt).schema
    primary_keys = ["rank", "synced_at"]


class GlobalTopTracksDailyStream(_PlaylistTracksStream):
    """Define global top tracks daily stream."""

    name = "global_top_tracks_daily_stream"
    path = "/playlists/37i9dQZEVXbMDoHDwVN2tF"
    primary_keys = ["rank", "synced_at"]


class GlobalTopTracksWeeklyStream(_PlaylistTracksStream):
    """Define global top tracks weekly stream."""

    name = "global_top_tracks_weekly_stream"
    path = "/playlists/37i9dQZEVXbNG2KDcFcKOF"
    primary_keys = ["rank", "synced_at"]


class GlobalViralTracksDailyStream(_PlaylistTracksStream):
    """Define global viral tracks daily stream."""

    name = "global_viral_tracks_daily_stream"
    path = "/playlists/37i9dQZEVXbLiRSasKsNU9"
    primary_keys = ["rank", "synced_at"]


class UserSavedTracksStream(_PlaylistTracksStream):
    """Define global viral tracks daily stream."""

    name = "user_saved_track_streams"
    path = "/me/tracks"
    schema = TrackObject
    primary_keys = ["rank", "synced_at"]
