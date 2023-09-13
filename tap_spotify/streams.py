"""Stream type classes for tap-spotify."""

from datetime import datetime
from typing import Iterable

from singer_sdk.streams.rest import RESTStream

from tap_spotify.client import SpotifyStream
from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.audio_features import AudioFeaturesObject
from tap_spotify.schemas.track import TrackObject
from tap_spotify.schemas.utils.rank import Rank
from tap_spotify.schemas.utils.synced_at import SyncedAt


class _RankStream(RESTStream):
    """Define a rank stream."""

    rank = 1

    def post_process(self, row, context):
        """Apply rank integer to stream"""
        row = super().post_process(row, context)
        row["rank"] = self.rank
        self.rank += 1
        return row


class _SyncedAtStream(RESTStream):
    """Define a synced at stream."""

    synced_at = datetime.utcnow()

    def post_process(self, row, context):
        """Apply synced at datetime to stream"""
        row = super().post_process(row, context)
        row["synced_at"] = self.synced_at
        return row


class _TracksStream(SpotifyStream):
    """Define a track stream."""

    def get_records(self, context):
        # get all track records
        track_records = list(super().request_records(context))

        # get all audio features records
        # instantiate audio features stream inline and request records
        audio_features_stream = _AudioFeaturesStream(self, track_records)
        audio_features_records = audio_features_stream.request_records(context)

        # merge track and audio features records
        for track, audio_features in zip(track_records, audio_features_records):

            # account for tracks with `null` audio features
            row = {**(audio_features or {}), **track}
            yield self.post_process(row, context)


class _AudioFeaturesStream(SpotifyStream):
    """Define an audio features stream."""

    name = "_audio_features_stream"
    path = "/audio-features"
    records_jsonpath = "$.audio_features[*]"
    schema = AudioFeaturesObject.schema

    def __init__(self, tracks_stream: _TracksStream, track_records: Iterable[dict]):
        super().__init__(tracks_stream._tap)
        self._track_records = track_records

    def get_url_params(self, *args, **kwargs):
        return {"ids": ",".join([track["id"] for track in self._track_records])}


class _UserTopItemsStream(_RankStream, _SyncedAtStream, SpotifyStream):
    """Define user top items stream."""

    time_range = "medium_term"
    limit = 49

    def get_url_params(self, context, next_page_token):
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


class _UserTopTracksStream(_TracksStream, _UserTopItemsStream):
    """Define user top tracks stream."""

    path = "/me/top/tracks"
    schema = TrackObject.extend_with(Rank, SyncedAt, AudioFeaturesObject).schema


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


class _PlaylistTracksStream(_RankStream, _SyncedAtStream, _TracksStream):
    """Define playlist tracks stream."""

    records_jsonpath = "$.tracks.items[*].track"
    schema = TrackObject.extend_with(Rank, SyncedAt, AudioFeaturesObject).schema
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


class UserSavedTracksStream(_SyncedAtStream, SpotifyStream):
    """Define user saved tracks stream."""

    name = "user_saved_tracks_stream"
    path = "/me/tracks"
    primary_keys = ["id", "synced_at"]
    limit = 50
    schema = TrackObject.extend_with(SyncedAt).schema
    records_jsonpath = "$.items[*].track"
