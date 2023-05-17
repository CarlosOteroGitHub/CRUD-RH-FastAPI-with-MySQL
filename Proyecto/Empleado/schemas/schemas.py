from datetime import date
from lib2to3.pytree import Base
from typing import Optional
from pydantic import BaseModel

class EmpleadoSchema(BaseModel):
    id: Optional[str]
    nombre: str
    nacimiento: date
    correo: str
    password: str
    descripcion: str
    departamento_id: str

    class Config:
        orm_mode = True