"""Schema definition for synced at schema wrapper"""

from tap_spotify.schemas.utils.schema_extender import SchemaExtender

from singer_sdk.typing import PropertiesList, Property, DateTimeType


class SyncedAt(SchemaExtender):

    schema = PropertiesList(
        Property("synced_at", DateTimeType),
    ).to_dict()
