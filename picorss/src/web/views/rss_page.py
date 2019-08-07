import flask
import inject
from flask import request

from picorss.src.application import queries, use_cases

bp = flask.Blueprint("rss_page", __name__)


@bp.route("/rss_pages", methods=["GET"])
def index() -> str:
    query = inject.instance(queries.GettingRssPagesQuery)
    result = query.execute()
    return flask.render_template("rss_pages.html", rss_pages=result.rss_pages)


@bp.route("/rss_pages/<int:page_id>", methods=["GET"])
def show_page(page_id: int):
    query = inject.instance(queries.GettingRssPageQuery)
    rss_page = query.execute(page_id)

    import feedparser
    data = feedparser.parse(rss_page.url)
    titles = [(article_id, e["title"]) for article_id, e in enumerate(data["entries"])]

    return flask.render_template("rss_page.html", rss_page=rss_page, titles=titles)


@bp.route("/rss_pages/<int:page_id>/article/<int:article_relative>", methods=["GET"])
def show_single_post(page_id: int, article_relative: int):
    query = inject.instance(queries.GettingRssPageQuery)
    rss_page = query.execute(page_id)

    import feedparser
    data = feedparser.parse(rss_page.url)

    article = data["entries"][article_relative]
    title = article["title"]
    text = flask.Markup(article["content"][0]["value"])

    return flask.render_template("single_post.html", rss_page=rss_page, title=title, text=text)


@bp.route("/rss_pages/add", methods=["POST"])
def add() -> str:
    use_cases.AddingRssPageUseCase().execute(
        use_cases.AddingRssPageUseCase.InputDTO(url=request.form["url"])
    )
    return flask.redirect(flask.url_for("rss_page.index"))
