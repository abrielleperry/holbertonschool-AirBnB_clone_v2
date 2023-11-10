#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """returns list of City instances upon state_id"""
            cities_list = []
            for obj in list(models.storage.all(City).values()):
                if obj.state_id == self.id:
                    cities_list.append(obj)
            return cities_list
