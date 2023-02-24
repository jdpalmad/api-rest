from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

subject_app = Table("subject_app", meta,Column("id", Integer, primary_key = True ), Column("subject", String(255)), 
    Column("specialty", String(255)), )

meta.create_all(engine)