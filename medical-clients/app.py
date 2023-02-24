from fastapi import FastAPI
from routes.user import user
from routes.appointment import appointment
from routes.subject import subject

app = FastAPI(
    title="Med Clients API",
    description="This is an API for a medical clients app",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
        }, {
        "name": "appointments",
        "description": "appointments routes"
        },{
        "name": "subjects",
        "description": "subjects routes"
        }], 
)
app.include_router(user)
app.include_router(appointment)
app.include_router(subject)