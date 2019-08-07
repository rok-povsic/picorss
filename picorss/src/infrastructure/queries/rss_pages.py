from sqlalchemy import orm

from picorss.src.application import queries
from picorss.src.infrastructure import models

import feedparser


class ORMGettingRssPageQuery(queries.GettingRssPageQuery):
    def __init__(self, session: orm.Session):
        self._session = session

    def execute(self, page_id: int) -> queries.GettingRssPageQuery.OutputDto:
        rss_page = self._session.query(models.RssPage).filter_by(id=page_id).one()
        return _translate_to_dto(rss_page)


class ORMGettingRssPagesQuery(queries.GettingRssPagesQuery):
    def __init__(self, session: orm.Session):
        self._session = session

    def execute(self) -> queries.GettingRssPagesQuery.OutputDto:
        rss_pages = self._session.query(models.RssPage).all()
        output_dto = [_translate_to_dto(rss_page) for rss_page in rss_pages]
        return queries.GettingRssPagesQuery.OutputDto(rss_pages=output_dto)


def _translate_to_dto(rss_page: models.RssPage) -> queries.GettingRssPageQuery.OutputDto:
    return queries.GettingRssPageQuery.OutputDto(id=rss_page.id, url=rss_page.url)

