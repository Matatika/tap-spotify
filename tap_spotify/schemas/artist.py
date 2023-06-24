"""Schema definitions for artist objects"""

from singer_sdk.typing import (
    ArrayType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_spotify.schemas.external import ExternalUrlObject
from tap_spotify.schemas.followers import FollowersObject
from tap_spotify.schemas.image import ImageObject
from tap_spotify.schemas.utils.custom_object import CustomObject


class ArtistObject(CustomObject):
    """https://developer.spotify.com/documentation/web-api/reference/#object-artistobject"""

    properties = PropertiesList(
        Property("external_urls", ExternalUrlObject),
        Property("followers", FollowersObject),
        Property("genres", ArrayType(StringType)),
        Property("href", StringType),
        Property("id", StringType),
        Property("images", ArrayType(ImageObject)),
        Property("name", StringType),
        Property("popularity", IntegerType),
        Property("type", StringType),
        Property("uri", StringType),
    )
