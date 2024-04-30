"""Schema definitions for external objects."""

from singer_sdk import typing as th

ExternalIdObject = th.PropertiesList(
    th.Property("ean", th.StringType),
    th.Property("isrc", th.StringType),
    th.Property("upc", th.StringType),
)

ExternalUrlObject = th.PropertiesList(
    th.Property("spotify", th.StringType),
)
