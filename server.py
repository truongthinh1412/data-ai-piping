import func.csv_processor as csv_processor
import func.lead as lead
from fastapi import FastAPI
import json
import asyncio
import requests
import pandas as pd

app = FastAPI()


@app.on_event("startup")
async def app_init():
  await lead.init()

@app.post("/lead/")
async def create_lead():
  url = "http://localhost:8002/linkedin/data?email=124"
  headers = {
    'accept': 'application/json'
  }
  response = requests.request("GET", url, headers=headers)
  data = response.json()
  if data is None:
    return None
  if "person" in data:
    person = data["person"]
    first_name = person.get("firstName", None)
    last_name = person.get("lastName", None)
    photo_url = person.get("photoUrl", None)
    email = None
    if person["emails"] is not None and len(person["emails"]) > 0:
      email = person["emails"][0]
    
    df = csv_processor.load_csv()
    field_of_study = []
    if "schools" in person:
      schools = person["schools"]
      if schools["educationsCount"] > 0:
        for school in schools["educationHistory"]:
            fos = school.get("fieldOfStudy", None)
            if fos is not None:
              result = df.loc[df['field_of_study'] == fos]
              for index, row in result.iterrows():
                field_of_study.append(row["academic_field"])
      
  company_type = None
  if "company" in data:
    e_count = data["company"].get("employeeCount", 0)
    if e_count > 0 and e_count <= 50:
      company_type = "Startup"
    elif e_count > 50 and e_count <= 1000:
      company_type = "Mid Market"
    else:
      company_type = "Multi National Company"    
  
  lead_id = await lead.create_lead(first_name, last_name, email, photo_url, field_of_study, company_type)
  return {"id" : lead_id}

@app.get("/lead/")
async def get_lead_info(lead_id: str):
  lead_result = await lead.get_lead_by_id(lead_id)
  return lead_result

