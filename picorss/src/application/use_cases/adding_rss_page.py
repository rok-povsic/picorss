import attr
import inject

from picorss.src.application import repositories
from picorss.src.domain import entities


class AddingRssPageUseCase:

    @attr.s
    class InputDTO:
        url: str = attr.ib()

    _rss_page_repo = inject.attr(repositories.RssPageRepo)

    def execute(self, input_dto: InputDTO) -> None:
        self._rss_page_repo.save(entities.RssPage(url=input_dto.url))

