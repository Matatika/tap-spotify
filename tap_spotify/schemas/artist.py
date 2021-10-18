"""Schema definitions for artist objects"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    ArrayType,
    CustomType,
    IntegerType,
    StringType,
)

from tap_spotify.schemas.external import ExternalUrlObject
from tap_spotify.schemas.followers import FollowersObject
from tap_spotify.schemas.image import ImageObject


class ArtistObject(CustomType):
    """https://developer.spotify.com/documentation/web-api/reference/#object-artistobject"""

    schema = PropertiesList(
        Property("external_urls", ExternalUrlObject()),
        Property("followers", FollowersObject()),
        Property("genres", ArrayType(StringType)),
        Property("href", StringType),
        Property("id", StringType),
        Property("images", ArrayType(ImageObject())),
        Property("name", StringType),
        Property("popularity", IntegerType),
        Property("type", StringType),
        Property("uri", StringType),
    ).to_dict()

    def __init__(self):
        super().__init__(self.schema)
