"""Schema definition for synced at schema wrapper"""

from singer_sdk.typing import PropertiesList, Property, DateTimeType

from tap_spotify.schemas.utils.custom_object import CustomObject


class SyncedAt(CustomObject):
    properties = PropertiesList(
        Property("synced_at", DateTimeType),
    )
