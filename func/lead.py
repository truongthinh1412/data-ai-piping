from typing import Optional, List
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
    academic_field: List[str] = []
    company_type: Optional[str] = None

    class Settings:
        collection = "leads"

class LeadResult():
    
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    academic_field: List[str] = []
    company_type: Optional[str] = None

    def __init__(self, firstname, lastname, email, academic_field, company_type):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.academic_field = academic_field
        self.company_type = company_type
        
async def init():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://root:example@localhost:27017/")
    database = client["local"]
    await init_beanie(database, document_models=[Lead])

async def create_lead(first_name, last_name, email, photo_url, academic_field, company_type):

    lead = Lead(
        first_name=first_name,
        last_name=last_name,
        email=email,
        photo_url=photo_url,
        academic_field=academic_field,
        company_type=company_type
    )
    await lead.insert()
    print(f"Lead created with id: {lead.id}")
    return lead.id

async def get_lead_by_id(lead_id: str):
    lead = await Lead.get(lead_id)
    if not lead:
        return None
    lead_result = LeadResult(firstname=lead.first_name, lastname=lead.last_name, email=lead.email, academic_field=lead.academic_field, company_type=lead.company_type)
    return lead_result

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

# async def main():
#     await init()
#     lead_id = await create_lead()
#     print(lead_id)
#     lead_email = await get_lead_email_by_id(lead_id=lead_id)
#     print(lead_email)

# asyncio.run(main())