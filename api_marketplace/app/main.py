from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
from fastapi.templating import Jinja2Templates
from fastapi import Request
import httpx

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/provider", response_class=HTMLResponse)
async def get_provider_page(request: Request):
    return templates.TemplateResponse("provider.html", {"request": request})

@app.post("/provider/upload")
async def upload_api(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"data/apis/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    api_data = schemas.APIBase(name=file.filename, path=file_location)
    crud.create_api(db=db, api=api_data)
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

@app.get("/customer", response_class=HTMLResponse)
async def get_customer_page(request: Request, db: Session = Depends(get_db)):
    apis = crud.get_apis(db)
    return templates.TemplateResponse("customer.html", {"request": request, "apis": apis})

@app.get("/customer/download/{api_id}")
async def download_api(api_id: int, db: Session = Depends(get_db)):
    api = crud.get_api(db, api_id=api_id)
    if not api:
        raise HTTPException(status_code=404, detail="API not found")
    return {"path": api.path, "name": api.name}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:5000/api/events/")
        events = response.json()
    return templates.TemplateResponse("home.html", {"request": request, "events": events})

@app.get("/api/events/")
async def get_events():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:5000/api/events/")
        return response.json()