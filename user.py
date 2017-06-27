from base import *
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ ='users'
    firstname = Column(String, 'firstname')

