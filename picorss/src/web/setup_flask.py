import flask
import sqlalchemy
from sqlalchemy import orm

from picorss.src.web import global_inject
from picorss.src.web.views import rss_page_bp

app = flask.Flask(__name__)
app.debug = True
app.secret_key = b"FIXME"

app.register_blueprint(rss_page_bp)

engine = sqlalchemy.create_engine(f"sqlite:///data/test_db.sqlite", echo=True)

Session = orm.scoped_session(orm.sessionmaker(bind=engine))


@app.teardown_appcontext
def teardown_appcontext(exception):
    Session.remove()


global_inject.inject_dependencies(Session)
