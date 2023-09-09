"""Schema definitions for external objects"""

from singer_sdk import typing as th

from tap_spotify.schemas.utils.custom_object import CustomObject


class ExternalIdObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("ean", th.StringType),
        th.Property("isrc", th.StringType),
        th.Property("upc", th.StringType),
    )


class ExternalUrlObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("spotify", th.StringType),
    )
