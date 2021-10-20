"""Schema definitions for image objects"""

from singer_sdk.typing import PropertiesList, Property, IntegerType, StringType

from tap_spotify.schemas.utils.custom_object import CustomObject


class ImageObject(CustomObject):
    """https://developer.spotify.com/documentation/web-api/reference/#object-imageobject"""

    properties = PropertiesList(
        Property("height", IntegerType),
        Property("url", StringType),
        Property("width", IntegerType),
    )
