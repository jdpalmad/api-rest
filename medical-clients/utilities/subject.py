from fastapi import status, Response
from config.db import meta, engine
from sqlalchemy import text
from config.db import conn
from models.subject import subject_app

def subjects_create_table():
    conn.execute(text("DROP TABLE IF EXISTS subject_app"))
    conn.commit()
    meta.create_all(engine)
    subject_list = conn.execute(text("SELECT DISTINCT subject FROM appointments ")).scalars().all()
    for subject_iter in subject_list:
        specialty_iter = conn.execute(text("SELECT DISTINCT specialty FROM appointments WHERE subject = :x"),{'x':subject_iter}).scalars().all()[0]
        conn.execute(subject_app.insert().values(subject=subject_iter, specialty=specialty_iter))
        conn.commit()
    return Response(status_code=status.HTTP_201_CREATED)


