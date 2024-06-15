from fastapi import FastAPI, UploadFile, File, HTTPException
from pymongo import MongoClient
import gridfs
import uvicorn
from fastapi.responses import StreamingResponse
from bson import ObjectId

app = FastAPI()

# MongoDB connection
client = MongoClient('mongodb://root:example@localhost:27017/')
db = client['local']
fs = gridfs.GridFS(db)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Read file contents
        contents = await file.read()
        
        # Save to GridFS
        file_id = fs.put(contents, filename=file.filename)
        return {"file_id": str(file_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{file_id}")
async def download_file(file_id: str):
    try:
        # Retrieve the file from GridFS
        grid_out = fs.get(ObjectId(file_id))
        return StreamingResponse(grid_out, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={grid_out.filename}"})
    except Exception as e:
        raise HTTPException(status_code=404, detail="File not found")

