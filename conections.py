from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

load_dotenv()

DB_OWNER = os.getenv('DB_OWNER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

engine = create_engine(f'postgresql://{DB_OWNER}:{DB_PASSWORD}@localhost:5432/apikeytest')

Session = sessionmaker(engine)
session = Session()

