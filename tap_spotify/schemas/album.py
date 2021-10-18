"""Schema definitions for album objects"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    ArrayType,
    CustomType,
    IntegerType,
    StringType,
)

from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.external import ExternalUrlObject
from tap_spotify.schemas.image import ImageObject
from tap_spotify.schemas.restriction import RestrictionObject as AlbumRestrictionObject


class AlbumObject(CustomType):
    """https://developer.spotify.com/documentation/web-api/reference/#object-albumbase"""

    schema = PropertiesList(
        Property("album_type", StringType),
        Property("artists", ArrayType(ArtistObject())),
        Property("available_markets", ArrayType(StringType)),
        Property("external_urls", ExternalUrlObject()),
        Property("href", StringType),
        Property("id", StringType),
        Property("images", ArrayType(ImageObject())),
        Property("name", StringType),
        Property("release_date", StringType),
        Property("release_date_precision", StringType),
        Property("restrictions", AlbumRestrictionObject()),
        Property("total_tracks", IntegerType),
        Property("type", StringType),
        Property("uri", StringType),
    ).to_dict()

    def __init__(self):
        super().__init__(self.schema)
