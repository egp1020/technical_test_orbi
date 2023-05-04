from sqlalchemy.orm import Session

from app.models import APIModel


def log_api_call(session: Session, timestamp, endpoint, params, result):
    api_model = APIModel(
        timestamp=timestamp,
        endpoint=endpoint,
        params=params,
        result=result,
    )
    session.add(api_model)
    session.commit()
    session.refresh(api_model)
    return api_model
