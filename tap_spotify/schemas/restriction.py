"""Schema definitions for restriction objects"""

from singer_sdk.typing import PropertiesList, Property, StringType

from tap_spotify.schemas.utils.custom_object import CustomObject


class RestrictionObject(CustomObject):
    properties = PropertiesList(
        Property("reason", StringType),
    )
