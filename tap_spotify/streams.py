"""Stream type classes for tap-spotify."""

from tap_spotify.client import SpotifyStream
from tap_spotify.schemas.track import TrackObject


class UserTopTracksStream(SpotifyStream):
    """Define user top tracks stream."""

    name = "user_top_tracks"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    schema = TrackObject.schema
