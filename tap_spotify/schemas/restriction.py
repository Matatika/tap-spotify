"""Schema definitions for restriction objects."""

from singer_sdk import typing as th

from tap_spotify.schemas.utils.custom_object import CustomObject


class RestrictionObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("reason", th.StringType),
    )
