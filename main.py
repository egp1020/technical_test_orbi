import logging
from datetime import datetime

from fastapi import BackgroundTasks, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import api, database, schemas, sessions

logging.basicConfig(level=logging.INFO)

app = FastAPI()


def process_api_call(session: Session, endpoint: str, params: dict, result: dict):
    timestamp = datetime.utcnow()
    sessions.log_api_call(session, timestamp, endpoint, params, result)


@app.post("/create_hubspot_contact")
async def create_hubspot_contact(
    contact: schemas.ContactSchema, background_tasks: BackgroundTasks
):
    result = api.create_hubspot_contact(contact.dict())
    if result.status != "error":
        background_tasks.add_task(
            process_api_call,
            database.session_local(),
            "/create_hubspot_contact",
            contact.dict(),
            result.to_dict(),
        )
        return result.to_dict()
    else:
        raise HTTPException(status_code=400, detail="Error creating contact in HubSpot")


@app.post("/sync_contacts")
async def sync_contacts(background_tasks: BackgroundTasks):
    contacts = api.get_hubspot_contacts().results
    created_tasks = []

    for contact in contacts:
        if not contact.properties.get("estado_clickup"):
            task_title = f"{contact.properties['firstname']} {contact.properties['lastname']} - {contact.properties['email']}"
            task_description = f"Phone: {contact.properties['phone']}\nWebsite: {contact.properties['website']}"
            task = api.create_clickup_task(task_title, task_description)
            created_tasks.append(task)

    background_tasks.add_task(
        process_api_call,
        database.session_local(),
        "/sync_contacts",
        {},
        {"created_tasks": len(created_tasks)},
    )
    return {"created_tasks": len(created_tasks)}
