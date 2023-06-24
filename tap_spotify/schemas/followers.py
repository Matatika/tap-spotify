"""Schema definitions for followers objects"""

from singer_sdk.typing import IntegerType, PropertiesList, Property, StringType

from tap_spotify.schemas.utils.custom_object import CustomObject


class FollowersObject(CustomObject):
    properties = PropertiesList(
        Property("href", StringType),
        Property("total", IntegerType),
    )
