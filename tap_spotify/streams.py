"""Stream type classes for tap-spotify."""

from typing import Any, Dict, Optional

from tap_spotify.client import SpotifyStream
from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.track import TrackObject


class UserTopTracksShortTermStream(SpotifyStream):
    """Define user top tracks short-term stream."""

    name = "user_top_tracks_st"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = TrackObject.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "short_term"
        return params


class UserTopTracksMediumTermStream(SpotifyStream):
    """Define user top tracks medium-term stream."""

    name = "user_top_tracks_mt"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = TrackObject.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "medium_term"
        return params


class UserTopTracksLongTermStream(SpotifyStream):
    """Define user top tracks long-term stream."""

    name = "user_top_tracks_lt"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = TrackObject.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "long_term"
        return params


class UserTopArtistsShortTermStream(SpotifyStream):
    """Define user top artists short-term stream."""

    name = "user_top_artists_st"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = ArtistObject.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "short_term"
        return params


class UserTopArtistsMediumTermStream(SpotifyStream):
    """Define user top artists medium-term stream."""

    name = "user_top_artists_mt"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = ArtistObject.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "medium_term"
        return params


class UserTopArtistsLongTermStream(SpotifyStream):
    """Define user top artists long-term stream."""

    name = "user_top_artists_lt"
    path = "/me/top/artists"
    primary_keys = ["id"]
    replication_key = None
    schema = ArtistObject.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["time_range"] = "long_term"
        return params


class _PlaylistTracksStream(SpotifyStream):
    """Define playlist tracks stream."""

    records_jsonpath = "$.tracks.items[*].track"
    primary_keys = ["id"]
    schema = TrackObject.schema


class GlobalTopTracksDailyStream(_PlaylistTracksStream):
    """Define global top tracks daily stream."""

    name = "global_top_tracks_daily"
    path = "/playlists/37i9dQZEVXbMDoHDwVN2tF"


class GlobalTopTracksWeeklyStream(_PlaylistTracksStream):
    """Define global top tracks weekly stream."""

    name = "global_top_tracks_weekly"
    path = "/playlists/37i9dQZEVXbNG2KDcFcKOF"


class GlobalViralTracksDailyStream(_PlaylistTracksStream):
    """Define global viral tracks daily stream."""

    name = "global_viral_tracks_daily"
    path = "/playlists/37i9dQZEVXbLiRSasKsNU9"
