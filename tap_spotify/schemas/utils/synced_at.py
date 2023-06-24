"""Schema definition for synced at schema wrapper"""

from singer_sdk.typing import DateTimeType, PropertiesList, Property

from tap_spotify.schemas.utils.custom_object import CustomObject


class SyncedAt(CustomObject):
    properties = PropertiesList(
        Property("synced_at", DateTimeType),
    )
