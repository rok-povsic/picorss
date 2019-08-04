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
def show(page_id: int):
    query = inject.instance(queries.GettingRssPageQuery)
    rss_page = query.execute(page_id)
    return flask.render_template("rss_page.html", rss_page=rss_page)


@bp.route("/rss_pages/add", methods=["POST"])
def add() -> str:
    use_cases.AddingRssPageUseCase().execute(
        use_cases.AddingRssPageUseCase.InputDTO(url=request.form["url"])
    )
    return flask.redirect(flask.url_for("rss_page.index"))
