from db import conn
from pathlib import Path
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from fastapi import APIRouter, Request, Response, status
from Proyecto.Departamento.schemas.schemas import DepartamentoSchema
from Proyecto.Departamento.models.models import departamento as DepartamentoModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

routes = APIRouter()

base_path = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(base_path / "../templates"))

@routes.get('/departamentos', response_class=HTMLResponse, tags=["Departamentos"])
async def index(request: Request):
    return templates.TemplateResponse("departamento.html", {"request": request})

@routes.get('/api/departamentos', response_model=List[DepartamentoSchema], tags=["Departamentos"])
async def show(request: Request):
    return conn.execute(DepartamentoModel.select()).fetchall()

@routes.post('/api/departamentos', response_model=DepartamentoSchema, tags=["Departamentos"])
async def save(departamento: DepartamentoSchema):
    nuevo_departamento = {"nombre": departamento.nombre}
    result = conn.execute(DepartamentoModel.insert().values(nuevo_departamento))
    return conn.execute(DepartamentoModel.select().where(DepartamentoModel.c.id == result.lastrowid)).first()

@routes.get('/api/departamentos/{id}', response_model=DepartamentoSchema, tags=["Departamentos"])
async def showId(id: str):
    return conn.execute(DepartamentoModel.select().where(DepartamentoModel.c.id == id)).first()

@routes.put('/api/departamentos/{id}', response_model=DepartamentoSchema, tags=["Departamentos"])
def update(id: str, departamento: DepartamentoSchema):
    conn.execute(DepartamentoModel.update().values(nombre=departamento.nombre).where(DepartamentoModel.c.id == id))
    return conn.execute(DepartamentoModel.select().where(DepartamentoModel.c.id == id)).first()

@routes.delete('/api/departamentos/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Departamentos"])
async def delete(id: str):
    conn.execute(DepartamentoModel.delete().where(DepartamentoModel.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)