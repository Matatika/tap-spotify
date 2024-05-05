"""Schema definition for synced at schema wrapper."""

from singer_sdk import typing as th

SyncedAt = th.PropertiesList(
    th.Property("synced_at", th.DateTimeType),
)
