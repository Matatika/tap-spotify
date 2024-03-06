"""Schema definitions for audio features objects."""

from singer_sdk.typing import (
    IntegerType,
    NumberType,
    PropertiesList,
    Property,
    StringType,
)

from tap_spotify.schemas.utils.custom_object import CustomObject


class AudioFeaturesObject(CustomObject):
    properties = PropertiesList(
        Property("acousticness", NumberType),
        Property("analysis_url", StringType),
        Property("danceability", NumberType),
        Property("duration_ms", IntegerType),
        Property("energy", NumberType),
        Property("id", StringType),
        Property("instrumentalness", NumberType),
        Property("key", IntegerType),
        Property("liveness", NumberType),
        Property("loudness", NumberType),
        Property("mode", IntegerType),
        Property("speechiness", NumberType),
        Property("tempo", NumberType),
        Property("time_signature", IntegerType),
        Property("track_href", StringType),
        Property("type", StringType),
        Property("uri", StringType),
        Property("valence", NumberType),
    )
