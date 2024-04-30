"""Schema definition for rank schema wrapper."""

from singer_sdk import typing as th

Rank = th.PropertiesList(
    th.Property("rank", th.IntegerType),
)
