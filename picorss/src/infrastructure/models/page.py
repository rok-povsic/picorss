import sqlalchemy
from sqlalchemy.sql import sqltypes

from picorss.src.infrastructure.models import meta


class RssPage(meta.Base):
    __tablename__ = 'rsspage'

    id = sqlalchemy.Column(sqltypes.Integer, primary_key=True)
    url = sqlalchemy.Column(sqltypes.String, nullable=False)
