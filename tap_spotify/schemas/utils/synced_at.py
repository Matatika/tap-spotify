"""Schema definition for synced at schema wrapper"""

from singer_sdk import typing as th

from tap_spotify.schemas.utils.custom_object import CustomObject


class SyncedAt(CustomObject):
    properties = th.PropertiesList(
        th.Property("synced_at", th.DateTimeType),
    )
