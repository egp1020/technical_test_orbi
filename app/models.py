from sqlalchemy import JSON, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class APIModel(Base):
    __tablename__ = "api_model"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    endpoint = Column(String, nullable=False)
    params = Column(JSON, nullable=False)
    result = Column(JSON, nullable=False)
