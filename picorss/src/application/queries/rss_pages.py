import abc

import attr


class GettingRssPageQuery(metaclass=abc.ABCMeta):

    @attr.s
    class OutputDto:
        id: int = attr.ib()
        url: str = attr.ib()

    @abc.abstractmethod
    def execute(self, page_id: int) -> OutputDto:
        pass


class GettingRssPagesQuery(metaclass=abc.ABCMeta):

    @attr.s
    class OutputDto:
        rss_pages: GettingRssPageQuery.OutputDto = attr.ib()

    @abc.abstractmethod
    def execute(self) -> OutputDto:
        pass
