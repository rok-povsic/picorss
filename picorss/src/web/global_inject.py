import inject
import typing

from sqlalchemy import orm

from picorss.src.application import queries, repositories
from picorss.src.infrastructure import (
    queries as orm_queries,
    repositories as orm_repositories,
)


def inject_dependencies(Session: typing.Callable[[], orm.Session]):
    def inject_config(binder: inject.Binder) -> None:
        # Queries
        binder.bind(queries.GettingRssPagesQuery, orm_queries.ORMGettingRssPagesQuery(Session()))

        # Repositories
        binder.bind(repositories.RssPageRepo, orm_repositories.RssPageRepo(Session()))

    inject.configure(inject_config, bind_in_runtime=False)
