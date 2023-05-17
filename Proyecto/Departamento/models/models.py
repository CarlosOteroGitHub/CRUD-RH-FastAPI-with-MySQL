from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db import engine, meta

departamento = Table("departamento", meta, 
    Column("id", Integer, primary_key=True),
    Column("nombre", String(50))
)

meta.create_all(engine)