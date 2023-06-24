"""Schema definitions for album objects"""

from singer_sdk.typing import (
    ArrayType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.external import ExternalUrlObject
from tap_spotify.schemas.image import ImageObject
from tap_spotify.schemas.restriction import RestrictionObject as AlbumRestrictionObject
from tap_spotify.schemas.utils.custom_object import CustomObject


class AlbumObject(CustomObject):
    """https://developer.spotify.com/documentation/web-api/reference/#object-albumbase"""

    properties = PropertiesList(
        Property("album_type", StringType),
        Property("artists", ArrayType(ArtistObject)),
        Property("available_markets", ArrayType(StringType)),
        Property("external_urls", ExternalUrlObject),
        Property("href", StringType),
        Property("id", StringType),
        Property("images", ArrayType(ImageObject)),
        Property("name", StringType),
        Property("release_date", StringType),
        Property("release_date_precision", StringType),
        Property("restrictions", AlbumRestrictionObject),
        Property("total_tracks", IntegerType),
        Property("type", StringType),
        Property("uri", StringType),
    )
