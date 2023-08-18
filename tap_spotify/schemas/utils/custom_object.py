"""Base custom object defintion"""

from singer_sdk import typing as th
from singer_sdk.helpers._classproperty import classproperty


class CustomObject(th.JSONTypeHelper):
    properties: th.PropertiesList

    @classproperty
    def type_dict(cls):
        return cls.properties.to_dict()

    @classproperty
    def schema(cls):
        return cls.type_dict

    @classmethod
    def extend_with(cls, *extras: "CustomObject"):
        for e in extras:
            for _, p in e.properties.items():
                cls.properties.append(p)
        return cls
