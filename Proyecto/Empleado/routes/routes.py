from db import conn
from pathlib import Path
from typing import List
from cryptography.fernet import Fernet
from fastapi import APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_204_NO_CONTENT
from Proyecto.Empleado.schemas.schemas import EmpleadoSchema
from Proyecto.Empleado.models.models import empleado as EmpleadoModel

key = Fernet.generate_key()
f = Fernet(key)

routes = APIRouter()

base_path = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(base_path / "../templates"))

@routes.get('/empleados', response_class=HTMLResponse, tags=["Empleados"])
async def index(request: Request):
    return templates.TemplateResponse("empleado.html", {"request": request})

@routes.get('/api/empleados', response_model=List[EmpleadoSchema], tags=["Empleados"])
async def show(request: Request):
    return conn.execute(EmpleadoModel.select()).fetchall()

@routes.post('/api/empleados', response_model=EmpleadoSchema, tags=["Empleados"])
async def save(empleado: EmpleadoSchema):
    nuevo_empleado = {
        "nombre": empleado.nombre, 
        "nacimiento": empleado.nacimiento,
        "correo": empleado.correo,
        "password": f.encrypt(empleado.password.encode("utf-8")),
        "descripcion": empleado.descripcion,
        "departamento_id": empleado.departamento_id
        }
    result = conn.execute(EmpleadoModel.insert().values(nuevo_empleado))
    return conn.execute(EmpleadoModel.select().where(EmpleadoModel.c.id == result.lastrowid)).first()

@routes.get('/api/empleados/{id}', response_model=EmpleadoSchema, tags=["Empleados"])
async def showId(id: str):
    return conn.execute(EmpleadoModel.select().where(EmpleadoModel.c.id == id)).first()

@routes.put('/api/empleados/{id}', response_model=EmpleadoSchema, tags=["Empleados"])
def update(id: str, empleado: EmpleadoSchema):
    conn.execute(EmpleadoModel.update().values(
        nombre=empleado.nombre, 
        nacimiento=empleado.nacimiento, 
        correo=empleado.correo, 
        password=f.encrypt(empleado.password.encode("utf-8")), 
        descripcion=empleado.descripcion,
        departamento_id=empleado.departamento_id).where(EmpleadoModel.c.id == id))
    return conn.execute(EmpleadoModel.select().where(EmpleadoModel.c.id == id)).first()

@routes.delete('/api/empleados/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Empleados"])
async def delete(id: str):
    conn.execute(EmpleadoModel.delete().where(EmpleadoModel.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)