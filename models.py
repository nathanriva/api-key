from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Users(base):
    __tablename__ = 'users'
    username = Column(String(20), primary_key=True) 
    password = Column(String(100))


