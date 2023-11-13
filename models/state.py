#!/usr/bin/python3
""" holds class State"""
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if models.storage_t == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            ''' getter attribute for cities '''
            city_list = []
            all_cities = models.DBStorage.all(City).values()
            for city in all_cities:
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
