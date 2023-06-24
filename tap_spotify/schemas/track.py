"""Schema definitions for track objects"""

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_spotify.schemas.album import AlbumObject
from tap_spotify.schemas.artist import ArtistObject
from tap_spotify.schemas.external import ExternalIdObject, ExternalUrlObject
from tap_spotify.schemas.restriction import RestrictionObject as TrackRestrictionObject
from tap_spotify.schemas.utils.custom_object import CustomObject


class TrackObject(CustomObject):
    properties = PropertiesList(
        Property("album", AlbumObject),
        Property("artists", ArrayType(ArtistObject)),
        Property("available_markets", ArrayType(StringType)),
        Property("disc_number", IntegerType),
        Property("duration_ms", IntegerType),
        Property("explicit", BooleanType),
        Property("external_ids", ExternalIdObject()),
        Property("external_urls", ExternalUrlObject),
        Property("href", StringType),
        Property("id", StringType),
        Property("is_local", BooleanType),
        Property("is_playable", BooleanType),
        # Property("linked_from", TrackObject),
        Property("name", StringType),
        Property("popularity", IntegerType),
        Property("preview_url", StringType),
        Property("restrictions", TrackRestrictionObject),
        Property("track_number", IntegerType),
        Property("type", StringType),
        Property("uri", StringType),
    )
