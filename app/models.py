from sqlalchemy import JSON, Column, DateTime, Integer, String

from app.database import Base


class APIBase(Base):
    __tablename__ = "api_model"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    endpoint = Column(String, nullable=False)
    params = Column(JSON, nullable=False)
    result = Column(JSON, nullable=False)
