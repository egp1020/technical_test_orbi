import logging
from datetime import datetime

from fastapi import BackgroundTasks, Depends, FastAPI
from sqlalchemy.orm import Session

from app import hubspot_clickup
from app.database import get_db
from app.schemas import ContactSchema
from app.sessions import log_api_call

logging.basicConfig(level=logging.INFO)

app = FastAPI()


def process_api_call(session: Session, endpoint: str, params: dict, result: dict):
    timestamp = datetime.utcnow()
    log_api_call(session, endpoint, timestamp, params, result)


@app.post("/create_hubspot_contact")
async def create_hubspot_contact(
    contact: ContactSchema,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    response = await hubspot_clickup.create_hubspot_contact(contact)

    background_tasks.add_task(
        process_api_call, db, "/create_hubspot_contact", contact.json(), response
    )
    return response


@app.post("/sync_contacts")
async def sync_contacts(
    background_tasks: BackgroundTasks, db: Session = Depends(get_db)
):
    contacts = hubspot_clickup.get_hubspot_contacts().results
    created_tasks = []

    for contact in contacts:
        if not contact.properties.get("status_clickup"):
            task_title = f"{contact.properties['firstname']} {contact.properties['lastname']} - {contact.properties['email']}"
            task_description = f"Phone: {contact.properties['phone']}\nWebsite: {contact.properties['website']}"
            task = hubspot_clickup.create_clickup_task(task_title, task_description)
            created_tasks.append(task)

            # Actualizar la propiedad "status_clickup" en HubSpot
            updated_properties = {"status_clickup": "created"}
            hubspot_clickup.update_contact_properties(contact.id, updated_properties)

    background_tasks.add_task(
        process_api_call,
        db,
        "/sync_contacts",
        "",
        {"created_tasks": len(created_tasks)},
    )
    return {"created_tasks": len(created_tasks)}
