from requests import Response
from singer_sdk.pagination import BaseHATEOASPaginator


class BodyLinkPaginator(BaseHATEOASPaginator):
    def get_next_url(self, response: Response):
        data: dict = response.json()
        return data.get("next")
