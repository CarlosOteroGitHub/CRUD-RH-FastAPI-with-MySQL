from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

routes = APIRouter()

base_path = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(base_path / "../templates"))

@routes.get('/', response_class=HTMLResponse, tags=["Home"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})