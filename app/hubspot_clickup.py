import logging

from clickupython import client
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException

from app.config import CLICKUP_LIST_ID, CLICKUP_TOKEN, HUBSPOT_TOKEN
from app.schemas import ContactSchema

hubspot_client = HubSpot(access_token=HUBSPOT_TOKEN)
clickup_client = client.ClickUpClient(CLICKUP_TOKEN)


async def create_hubspot_contact(contact: ContactSchema):
    contact_model = SimplePublicObjectInput(
        properties={
            "email": contact.email,
            "firstname": contact.firstname,
            "lastname": contact.lastname,
            "phone": contact.phone,
            "website": contact.website,
        }
    )

    try:
        created_contact = hubspot_client.crm.contacts.basic_api.create(contact_model)
        logging.info(f"Contact created in HubSpot: {created_contact}")
    except ApiException as e:
        logging.error(f"An error occurred while creating the contact in HubSpot: {e}")
        return {"error": str(e)}

    return {"contact_id": created_contact.id}


def get_hubspot_contacts():
    return hubspot_client.crm.contacts.basic_api.get_all()


def create_clickup_task(title, description):
    task_data = {
        "name": title,
        "description": description,
        "list_id": CLICKUP_LIST_ID,
    }
    return clickup_client.create_task(task_data)
