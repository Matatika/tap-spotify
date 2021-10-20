"""Schema definition for rank schema wrapper"""

from singer_sdk.typing import PropertiesList, Property, IntegerType

from tap_spotify.schemas.utils.custom_object import CustomObject


class Rank(CustomObject):
    properties = PropertiesList(
        Property("rank", IntegerType),
    )
