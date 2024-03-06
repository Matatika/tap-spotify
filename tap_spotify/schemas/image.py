"""Schema definitions for image objects."""

from singer_sdk import typing as th

from tap_spotify.schemas.utils.custom_object import CustomObject


class ImageObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("height", th.IntegerType),
        th.Property("url", th.StringType),
        th.Property("width", th.IntegerType),
    )
