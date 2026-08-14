"""Schema definitions for restriction objects.

Copyright (c) 2026 Meltano.
"""

from singer_sdk import typing as th

RestrictionObject = th.PropertiesList(
    th.Property("reason", th.StringType),
)
