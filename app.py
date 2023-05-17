from fastapi import FastAPI
from Proyecto.Home.routes.routes import routes as routesHome
from Proyecto.Departamento.routes.routes import routes as routesDepartamento
from Proyecto.Empleado.routes.routes import routes as routesEmpleado

app = FastAPI(
    title="API Rest con MySQL y FastAPI",
    description="This program allows build an Web App with Python language",
    version="0.0.1",
    openapi_tags=[{
        "name": "API Rest MySQL y FastAPI",
        "description": "Rutas OpenAPI Doc"
    }]
)

app.include_router(routesHome)
app.include_router(routesDepartamento)
app.include_router(routesEmpleado)

#Programa Python con FastAPI que retorna un archivo HTML con la frase Hola Mundo!