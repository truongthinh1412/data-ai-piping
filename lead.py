from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field
from beanie import Document, init_beanie
import motor.motor_asyncio
import asyncio

class Lead(Document):
    id: str = Field(default_factory=lambda: uuid4().hex)
    status: int = 0
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    photo_url: Optional[str] = None

    class Settings:
        collection = "leads"

async def init():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://root:example@localhost:27017/")
    database = client["local"]
    await init_beanie(database, document_models=[Lead])

async def create_lead():
    lead = Lead(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"
    )
    await lead.insert()
    print(f"Lead created with id: {lead.id}")
    return lead.id

async def get_lead_by_id(lead_id: str):
    lead = await Lead.get(lead_id)
    print(lead)
    result = {
        "first_name": lead.first_name,
        "last_name": lead.last_name,
        "email": lead.email,
        "photo_url": lead.photo_url
    }
    return result

async def update_lead_status(lead_id: str, new_status: int):
    lead = await Lead.get(lead_id)
    if lead:
        lead.status = new_status
        await lead.save()
        print(f"Lead {lead_id} status updated to {new_status}")

async def delete_lead(lead_id: str):
    lead = await Lead.get(lead_id)
    if lead:
        await lead.delete()
        print(f"Lead {lead_id} deleted")

async def main():
    await init()
    lead_id = await create_lead()
    print(lead_id)
    lead = await get_lead_by_id(lead_id=lead_id)
    print(lead["email"])
    print(lead["photo_url"])
    # asyncio.run(update_lead_status("some_lead_id", 1))
    # asyncio.run(delete_lead("some_lead_id"))

asyncio.run(main())