from sqlalchemy.orm import Session

from app.models import APIBase


def log_api_call(session: Session, timestamp, endpoint, params, result):
    api_call_model = APIBase(
        timestamp=timestamp,
        endpoint=endpoint,
        params=params,
        result=result,
    )
    session.add(api_call_model)
    session.commit()
    session.refresh(api_call_model)
    return api_call_model
