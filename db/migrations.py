from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    first_name = Column(String(100), unique=False, nullable=True)
    last_name = Column(String(100), unique=False, nullable=True)
    email = Column(String(50), unique=True, nullable=True)
    password = Column(String(100), unique=False, nullable=False)


def create_tables(engine, table_name):
    if not engine.dialect.has_table(engine, table_name):
        Base.metadata.create_all(bind=engine)
    return engine.dialect.has_table(engine, table_name)
