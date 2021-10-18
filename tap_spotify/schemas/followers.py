"""Schema definitions for followers objects"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    CustomType,
    IntegerType,
    StringType,
)


class FollowersObject(CustomType):
    """https://developer.spotify.com/documentation/web-api/reference/#object-followersobject"""

    schema = PropertiesList(
        Property("href", StringType),
        Property("total", IntegerType),
    ).to_dict()

    def __init__(self):
        super().__init__(self.schema)
