#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from slqalchemy import Column, String, Integer, Datetime, Foreignkey
import sqlalchemy
from sqlalchemy.orm import relationship
from models.city import city

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable = False)
    
    cities = relationship("City", backref = "state", cascade = "delete")

