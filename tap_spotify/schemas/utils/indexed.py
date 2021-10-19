"""Schema definition for indexed schema wrapper"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    CustomType,
    IntegerType,
    JSONTypeHelper,
)


class Indexed(CustomType):

    schema = PropertiesList(
        Property("index", IntegerType),
    ).to_dict()

    def __init__(self, json_type: JSONTypeHelper = None) -> dict:
        if json_type:
            properties: dict = self.schema.get("properties")
            properties.update(json_type.type_dict.get("properties", {}))
            self.schema["properties"] = properties

        super().__init__(self.schema)
