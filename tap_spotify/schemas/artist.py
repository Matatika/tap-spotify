"""Schema definitions for artist objects."""

from singer_sdk import typing as th

from tap_spotify.schemas.external import ExternalUrlObject
from tap_spotify.schemas.followers import FollowersObject
from tap_spotify.schemas.image import ImageObject

ArtistObject = th.PropertiesList(
    th.Property("external_urls", ExternalUrlObject),
    th.Property("followers", FollowersObject),
    th.Property("genres", th.ArrayType(th.StringType)),
    th.Property("href", th.StringType),
    th.Property("id", th.StringType),
    th.Property("images", th.ArrayType(ImageObject)),
    th.Property("name", th.StringType),
    th.Property("popularity", th.IntegerType),
    th.Property("type", th.StringType),
    th.Property("uri", th.StringType),
)
