import attr


@attr.s
class RssPage:
    url: str = attr.ib()
