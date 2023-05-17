from sqlalchemy import Date, ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db import engine, meta

empleado = Table("empleado", meta, 
    Column("id", Integer, primary_key=True),
    Column("nombre", String(100)),
    Column("nacimiento", Date),
    Column("correo", String(100)),
    Column("password", String(100)),
    Column("descripcion", String(100)),
    Column("departamento_id", Integer, ForeignKey('departamento.id')),
)

meta.create_all(engine)