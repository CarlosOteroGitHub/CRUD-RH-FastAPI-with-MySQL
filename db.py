import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()
db_name = os.environ.get("DATABASE")

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/" + str(db_name))
meta = MetaData()
conn = engine.connect()