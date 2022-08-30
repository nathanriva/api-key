from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Users(base):
    __tablename__ = 'users'
    username = Column(String(20), primary_key=True) 
    password = Column(String(1000))
    admin = Column(Boolean)

