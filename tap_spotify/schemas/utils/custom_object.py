"""Base custom object defintion."""

from __future__ import annotations

from singer_sdk import typing as th
from typing_extensions import Self, override

# ruff: noqa: N805


class CustomObject(th.JSONTypeHelper):
    """Custom object."""

    properties: th.PropertiesList

    @th.DefaultInstanceProperty
    @override
    def type_dict(cls):
        return cls.properties.to_dict()

    @th.DefaultInstanceProperty
    def schema(cls):  # noqa: D102
        return cls.type_dict

    @classmethod
    def extend_with(cls, *extras: type[Self]) -> type[Self]:
        """Extend a custom object schema with other custom object types."""
        for e in extras:
            for _, p in e.properties.items():  # noqa: PERF102
                cls.properties.append(p)
        return cls
