#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


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
            from models import storage
            from models.city import City
            city_list = []
            all_cities = storage.all(City).values()
            for city in all_cities:
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
