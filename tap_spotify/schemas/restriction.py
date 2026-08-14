# Copyright (c) 2026 Meltano.

"""Schema definitions for restriction objects."""

from singer_sdk import typing as th

RestrictionObject = th.PropertiesList(
    th.Property("reason", th.StringType),
)
