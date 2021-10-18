"""Schema definitions for image objects"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    CustomType,
    IntegerType,
    StringType,
)


class ImageObject(CustomType):
    """https://developer.spotify.com/documentation/web-api/reference/#object-imageobject"""

    schema = PropertiesList(
        Property("height", IntegerType),
        Property("url", StringType),
        Property("width", IntegerType),
    ).to_dict()

    def __init__(self):
        super().__init__(self.schema)
