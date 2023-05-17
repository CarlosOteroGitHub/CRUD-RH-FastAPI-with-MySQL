from lib2to3.pytree import Base
from typing import Optional
from pydantic import BaseModel

class DepartamentoSchema(BaseModel):
    id: Optional[str]
    nombre: str

    class Config:
        orm_mode = True