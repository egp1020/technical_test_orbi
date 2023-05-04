from clickupython import client
from hubspot import HubSpot

from app.config import CLICKUP_LIST_ID, CLICKUP_TOKEN, HUBSPOT_TOKEN

hubspot_client = HubSpot(api_key=HUBSPOT_TOKEN)
clickup_client = client.ClickUpClient(CLICKUP_TOKEN)


def create_hubspot_contact(contact_data):
    return hubspot_client.crm.contacts.basic_api.create(contact_data)


def get_hubspot_contacts():
    return hubspot_client.crm.contacts.basic_api.get_all()


def create_clickup_task(title, description):
    task_data = {
        "name": title,
        "description": description,
        "list_id": CLICKUP_LIST_ID,
    }
    return clickup_client.create_task(task_data)
