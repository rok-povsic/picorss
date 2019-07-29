from sqlalchemy import orm

from picorss.src.application import repositories
from picorss.src.domain import entities
from picorss.src.infrastructure import models


class RssPageRepo(repositories.RssPageRepo):
    def __init__(self, session: orm.Session) -> None:
        self._session = session

    def save(self, rss_page: entities.RssPage) -> None:
        rss_page_model = models.RssPage(url=rss_page.url)
        self._session.add(rss_page_model)
        self._session.commit()
