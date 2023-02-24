from fastapi import APIRouter
from config.db import conn
from models.subject import subject_app
from schemas.subject import Subject
from schemas.appointment import Appointment
from sqlalchemy import text
from utilities.subject import *

subject = APIRouter()

@subject.get("/subjects", response_model=list[Subject], description='Update Table and see distinct subjects' 
    ,tags=["subjects"])
def subjects_get_all():
    subjects_create_table()
    return conn.execute(text("SELECT * from subject_app")).mappings().all()

@subject.get("/subjects/{id}",response_model = list[Appointment] ,tags=["subjects"], description="Get all the appointments of a subject")
def subject_expand(id:str):
    querysub = conn.execute(subject_app.select().where(subject_app.c.id == id)).mappings().first()['subject']
    return conn.execute(text("SELECT * FROM appointments WHERE subject = :y"),{'y': querysub}).mappings().all()

@subject.get("/subjects/{id}/total", tags=["subjects"], description="Frequency of a subject")
def subject_frequency(id:str):
    querysub = conn.execute(subject_app.select().where(subject_app.c.id == id)).mappings().first()['subject']
    print(querysub)
    return conn.execute(text("SELECT count(*) from appointments WHERE subject = :w"),{'w': querysub}).scalar()  