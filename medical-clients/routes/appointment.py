from fastapi import APIRouter, status, Response
from config.db import conn
from models.user import users
from models.appointment import appointments
from schemas.appointment import Appointment
appointment = APIRouter()

@appointment.get("/appointments", response_model=list[Appointment], 
    description="Get a list of all appointments", tags=["appointments"])
def get_appointments():
    return conn.execute(appointments.select()).mappings().all()

@appointment.post("/appointments/{id}",  response_model=Appointment, 
    description="Create a new appointment", tags=["appointments"])
def create_appointment(id:str, appointment:Appointment):
    queryname = conn.execute(users.select().where(users.c.id == id)).mappings().first()['name']
    new_appointment = {"userid":id, "name":queryname, "specialty":appointment.specialty, 
    "subject":appointment.subject, "date":appointment.date}
    result = conn.execute(appointments.insert().values(new_appointment))
    conn.commit()
    l_conn = conn.execute(appointments.select().where(appointments.c.id == result.lastrowid)).mappings().first()
    return l_conn

@appointment.get("/appointments/{id}", response_model=list[Appointment], 
    description="Get all appointments of an user id", tags=["appointments"])
def get_fullappointment(id:str):
    return conn.execute(appointments.select().where(appointments.c.userid == id)).mappings().all()

@appointment.get("/appointments/{userid}/{id}", response_model=Appointment, description="Get an appointment by id", 
    tags=["appointments"])
def get_appointment(userid:str, id:str):
    return conn.execute(appointments.select().where( 
        (appointments.c.id == id) & (appointments.c.userid == userid) )).mappings().first()

@appointment.put("/appointments/{userid}/{id}",response_model=Appointment ,description="Update an appointment by its id", 
    tags=["appointments"])
def update_appointment(userid:str, id:str, appointment:Appointment):
    conn.execute(appointments.update().where(appointments.c.id == id).values(
        specialty=appointment.specialty, subject=appointment.subject, date=appointment.date
    ))
    conn.commit()
    return conn.execute(appointments.select().where( 
        (appointments.c.id == id) & (appointments.c.userid == userid) )).mappings().first()

@appointment.get("/daily_appointments/{date}", response_model = list[Appointment] ,description="Get the appointments of a date",  
    tags=["appointments"])
def get_all_appointments(date:str):
    return conn.execute(appointments.select().where(appointments.c.date == date)).mappings().all()
    
@appointment.delete("/appointments/{userid}/{id}", status_code=status.HTTP_204_NO_CONTENT, 
    description="Delete an appointment by its id", tags=["appointments"])
def delete_appointment(userid:str, id:str):
    conn.execute(appointments.delete().where( 
        (appointments.c.id == id) & (appointments.c.userid == userid) ))
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

