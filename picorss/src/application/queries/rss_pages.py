import abc

import attr


class GettingRssPageQuery(metaclass=abc.ABCMeta):

    @attr.s
    class OutputDto:
        url: str = attr.ib()

    # TODO: Implement single RSS page query.


class GettingRssPagesQuery(metaclass=abc.ABCMeta):

    @attr.s
    class OutputDto:
        rss_pages: GettingRssPageQuery.OutputDto = attr.ib()

    @abc.abstractmethod
    def execute(self) -> OutputDto:
        pass
