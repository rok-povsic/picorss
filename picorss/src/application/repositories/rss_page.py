import abc

from picorss.src.domain import entities


class RssPageRepo:

    @abc.abstractmethod
    def save(self, rss_page: entities.RssPage) -> None:
        pass
