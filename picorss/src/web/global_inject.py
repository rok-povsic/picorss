import inject
import typing

from sqlalchemy import orm

from picorss.src.application import queries, repositories
from picorss.src.infrastructure import (
    queries as orm_queries,
    repositories as orm_repositories,
)


def inject_dependencies(Session: typing.Callable[[], orm.Session]):
    session = Session()

    def inject_config(binder: inject.Binder) -> None:
        # Queries
        binder.bind(queries.GettingRssPageQuery, orm_queries.ORMGettingRssPageQuery(session))
        binder.bind(queries.GettingRssPagesQuery, orm_queries.ORMGettingRssPagesQuery(session))

        # Repositories
        binder.bind(repositories.RssPageRepo, orm_repositories.RssPageRepo(session))

    inject.configure(inject_config, bind_in_runtime=False)
