"""Schema definitions for restriction objects"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    CustomType,
    StringType,
)


class RestrictionObject(CustomType):
    """
    AlbumRestrictionObject: https://developer.spotify.com/documentation/web-api/reference/#object-albumrestrictionobject
    TrackRestrictionObject: https://developer.spotify.com/documentation/web-api/reference/#object-trackrestrictionobject
    """

    schema = PropertiesList(
        Property("reason", StringType),
    ).to_dict()

    def __init__(self):
        super().__init__(self.schema)
