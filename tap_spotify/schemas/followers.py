"""Schema definitions for followers objects."""

from singer_sdk import typing as th

FollowersObject = th.PropertiesList(
    th.Property("href", th.StringType),
    th.Property("total", th.IntegerType),
)
