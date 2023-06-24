"""Schema definitions for image objects"""

from singer_sdk.typing import IntegerType, PropertiesList, Property, StringType

from tap_spotify.schemas.utils.custom_object import CustomObject


class ImageObject(CustomObject):
    properties = PropertiesList(
        Property("height", IntegerType),
        Property("url", StringType),
        Property("width", IntegerType),
    )
