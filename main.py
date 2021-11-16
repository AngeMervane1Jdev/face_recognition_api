from typing import List
import os
import uuid
import api
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(file: UploadFile = File(...)):

    file.filename=f"{uuid.uuid4()}.jpg"
    contents = await file.read() 

    fic=open(f"uploads/{file.filename}", "+wb")
    fic.write(contents)
    returned= {api.getFace(f"uploads/{file.filename}")}
    os.unlink(f"uploads/{file.filename}")
    return returned



@app.post("/register_file/")
async def get_files(file: UploadFile = File(...),):

    file.filename=f"{uuid.uuid4()}.jpg"
    contents = await file.read() 
    
    fic=open(f"knowImages/{file.filename}", "+wb")
    fic.write(contents)
    return "saved !!"



@app.post("/uploadfiles/")
async def create_upload_files(file: UploadFile = File(...)):
    return {"filename": [file.filename]}


@app.get("/")
async def main():
    content = """
                <body>
                    <form action="/files/" enctype="multipart/form-data" method="post">
                            <input name="file" type="file">
                            <input type="submit">
                    </form>
                </body>
              """
    return HTMLResponse(content=content)