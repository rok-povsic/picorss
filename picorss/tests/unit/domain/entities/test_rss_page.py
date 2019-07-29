import pytest

from picorss.src.domain import entities


@pytest.fixture()
def rss_page() -> entities.RssPage:
    return entities.RssPage(url="https://example.com")


def test_rss_page_has_url(rss_page: entities.RssPage) -> None:
    assert rss_page.url
