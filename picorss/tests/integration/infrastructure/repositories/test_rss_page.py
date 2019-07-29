import os

import sqlalchemy
from sqlalchemy import orm

from picorss.src.domain import entities
from picorss.src.infrastructure import repositories, models
from picorss.src.infrastructure.models import meta


class IntTestConnection:
    def __init__(self, tmp_path: str) -> None:
        self._file_path = f"{tmp_path}/test_db.sqlite"

        engine = sqlalchemy.create_engine(self.url, echo=True)

        Session = orm.sessionmaker(bind=engine)
        self.session: orm.Session = Session()

        meta.Base.metadata.create_all(engine)

    @property
    def url(self):
        return f"sqlite:///{self._file_path}"

    def __enter__(self) -> 'IntTestConnection':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        os.remove(self._file_path)


def test_rss_page_should_be_saved(tmp_path: str):
    with IntTestConnection(tmp_path) as conn:
        rss_page_repo = repositories.RssPageRepo(conn.session)
        rss_page_repo.save(entities.RssPage(url="https://example.com"))

        assert conn.session.query(models.RssPage).one().url == "https://example.com"
