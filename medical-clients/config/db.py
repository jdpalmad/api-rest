from sqlalchemy import create_engine, MetaData
from dotenv import dotenv_values
# Configuracion de la conexion a la base de datos

# Esta parte deberia estar en otro archivo con el fin de 
# respetar el principio de responsabilidad unica.
db_config = dotenv_values(".env")

# Creacion del motor de la base de datos
engine = create_engine(f"mysql+pymysql://"+db_config['USER']+":"+db_config['SQL_PASSWORD']+"@"+
        db_config['HOST']+":"+db_config['PORT']+"/"+db_config['DATABASE'])

meta = MetaData()
conn = engine.connect()


