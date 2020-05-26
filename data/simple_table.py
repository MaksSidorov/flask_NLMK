import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class SimpleTable(SqlAlchemyBase):
    __tablename__ = 'simpl_table'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    col1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    col2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    col3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    col4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    col5 = sqlalchemy.Column(sqlalchemy.String, nullable=True)


if __name__ == '__main__':
    print(1)
