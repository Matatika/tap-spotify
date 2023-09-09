"""Schema definitions for album objects"""

from singer_sdk import typing as th

from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.external import ExternalUrlObject
from tap_spotify.schemas.image import ImageObject
from tap_spotify.schemas.restriction import RestrictionObject as AlbumRestrictionObject
from tap_spotify.schemas.utils.custom_object import CustomObject


class AlbumObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("album_type", th.StringType),
        th.Property("artists", th.ArrayType(ArtistObject)),
        th.Property("available_markets", th.ArrayType(th.StringType)),
        th.Property("external_urls", ExternalUrlObject),
        th.Property("href", th.StringType),
        th.Property("id", th.StringType),
        th.Property("images", th.ArrayType(ImageObject)),
        th.Property("name", th.StringType),
        th.Property("release_date", th.StringType),
        th.Property("release_date_precision", th.StringType),
        th.Property("restrictions", AlbumRestrictionObject),
        th.Property("total_tracks", th.IntegerType),
        th.Property("type", th.StringType),
        th.Property("uri", th.StringType),
    )
