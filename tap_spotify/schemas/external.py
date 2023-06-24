"""Schema definitions for external objects"""

from singer_sdk.typing import PropertiesList, Property, StringType

from tap_spotify.schemas.utils.custom_object import CustomObject


class ExternalIdObject(CustomObject):
    properties = PropertiesList(
        Property("ean", StringType),
        Property("isrc", StringType),
        Property("upc", StringType),
    )


class ExternalUrlObject(CustomObject):
    properties = PropertiesList(
        Property("spotify", StringType),
    )
