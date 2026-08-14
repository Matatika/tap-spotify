"""Schema definitions for image objects."""

from singer_sdk import typing as th

ImageObject = th.PropertiesList(
    th.Property("height", th.IntegerType),
    th.Property("url", th.StringType),
    th.Property("width", th.IntegerType),
)
