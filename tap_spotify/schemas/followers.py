"""Schema definitions for followers objects.

Copyright (c) 2026 Meltano.
"""

from singer_sdk import typing as th

FollowersObject = th.PropertiesList(
    th.Property("href", th.StringType),
    th.Property("total", th.IntegerType),
)
