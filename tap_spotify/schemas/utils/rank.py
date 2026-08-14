"""Schema definition for rank schema wrapper.

Copyright (c) 2026 Meltano.
"""

from singer_sdk import typing as th

Rank = th.PropertiesList(
    th.Property("rank", th.IntegerType),
)
