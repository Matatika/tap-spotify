"""Schema definitions for restriction objects"""

from singer_sdk.typing import PropertiesList, Property, StringType

from tap_spotify.schemas.utils.custom_object import CustomObject


class RestrictionObject(CustomObject):
    """
    AlbumRestrictionObject: https://developer.spotify.com/documentation/web-api/reference/#object-albumrestrictionobject
    TrackRestrictionObject: https://developer.spotify.com/documentation/web-api/reference/#object-trackrestrictionobject
    """

    properties = PropertiesList(
        Property("reason", StringType),
    )
