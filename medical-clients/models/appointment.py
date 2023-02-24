from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

appointments = Table("appointments", meta,Column("id", Integer, primary_key = True), Column("userid", Integer) ,Column("name",String(255)), 
    Column("specialty", String(255)), Column("subject", String(255)), Column("date", String(255)), )

meta.create_all(engine)