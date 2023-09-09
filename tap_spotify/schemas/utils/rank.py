"""Schema definition for rank schema wrapper"""

from singer_sdk import typing as th

from tap_spotify.schemas.utils.custom_object import CustomObject


class Rank(CustomObject):
    properties = th.PropertiesList(
        th.Property("rank", th.IntegerType),
    )
