import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_uri = os.getenv("DATABASE_URI")

engine = create_engine(database_uri)
get_session = sessionmaker(bind=engine)
