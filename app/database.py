from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def create_tables():
    with engine.begin() as connection:
        Base.metadata.create_all(bind=engine, checkfirst=True)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


create_tables()
