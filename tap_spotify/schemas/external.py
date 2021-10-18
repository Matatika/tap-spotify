"""Schema definitions for external objects"""

from singer_sdk.typing import (
    PropertiesList,
    Property,
    CustomType,
    StringType,
)


class ExternalIdObject(CustomType):
    """https://developer.spotify.com/documentation/web-api/reference/#object-externalidobject"""

    schema = PropertiesList(
        Property("ean", StringType),
        Property("isrc", StringType),
        Property("upc", StringType),
    ).to_dict()

    def __init__(self):
        super(ExternalIdObject, self).__init__(self.schema)


class ExternalUrlObject(CustomType):
    """https://developer.spotify.com/documentation/web-api/reference/#object-externalurlobject"""

    schema = PropertiesList(
        Property("spotify", StringType),
    ).to_dict()

    def __init__(self):
        super().__init__(self.schema)
