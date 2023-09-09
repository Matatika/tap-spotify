from singer_sdk.pagination import BaseHATEOASPaginator


class BodyLinkPaginator(BaseHATEOASPaginator):
    def get_next_url(self, response):
        data: dict = response.json()
        return data.get("next")
