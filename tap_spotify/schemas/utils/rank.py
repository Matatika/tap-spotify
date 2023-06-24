"""Schema definition for rank schema wrapper"""

from singer_sdk.typing import IntegerType, PropertiesList, Property

from tap_spotify.schemas.utils.custom_object import CustomObject


class Rank(CustomObject):
    properties = PropertiesList(
        Property("rank", IntegerType),
    )
