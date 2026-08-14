"""Schema definitions for track objects."""

from singer_sdk import typing as th

from tap_spotify.schemas.album import AlbumObject
from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.external import ExternalIdObject, ExternalUrlObject
from tap_spotify.schemas.restriction import RestrictionObject as TrackRestrictionObject

TrackObject = th.PropertiesList(
    th.Property("album", AlbumObject),
    th.Property("artists", th.ArrayType(ArtistObject)),
    th.Property("available_markets", th.ArrayType(th.StringType)),
    th.Property("disc_number", th.IntegerType),
    th.Property("duration_ms", th.IntegerType),
    th.Property("explicit", th.BooleanType),
    th.Property("external_ids", ExternalIdObject),
    th.Property("external_urls", ExternalUrlObject),
    th.Property("href", th.StringType),
    th.Property("id", th.StringType),
    th.Property("is_local", th.BooleanType),
    th.Property("is_playable", th.BooleanType),
    # th.Property("linked_from", TrackObject),  # noqa: ERA001
    th.Property("name", th.StringType),
    th.Property("popularity", th.IntegerType),
    th.Property("preview_url", th.StringType),
    th.Property("restrictions", TrackRestrictionObject),
    th.Property("track_number", th.IntegerType),
    th.Property("type", th.StringType),
    th.Property("uri", th.StringType),
)
