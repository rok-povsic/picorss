from sqlalchemy import orm

from picorss.src.application import queries
from picorss.src.infrastructure import models


class ORMGettingRssPagesQuery(queries.GettingRssPagesQuery):
    def __init__(self, session: orm.Session):
        self._session = session

    def execute(self) -> queries.GettingRssPagesQuery.OutputDto:
        rss_pages = self._session.query(models.RssPage).all()
        output_dto = [self._translate_to_dto(rss_page) for rss_page in rss_pages]
        return queries.GettingRssPagesQuery.OutputDto(rss_pages=output_dto)

    def _translate_to_dto(self, rss_page: models.RssPage) -> queries.GettingRssPageQuery.OutputDto:
        return queries.GettingRssPageQuery.OutputDto(url=rss_page.url)

