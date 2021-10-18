"""Stream type classes for tap-spotify."""

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_spotify.client import SpotifyStream


class UserTopTracksStream(SpotifyStream):
    """Define user top tracks stream."""

    name = "user_top_tracks"
    path = "/me/top/tracks"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
        ),
        th.Property(
            "name",
            th.StringType,
        ),
    ).to_dict()
