"""Schema definitions for followers objects."""

from singer_sdk import typing as th

from tap_spotify.schemas.utils.custom_object import CustomObject


class FollowersObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("href", th.StringType),
        th.Property("total", th.IntegerType),
    )
