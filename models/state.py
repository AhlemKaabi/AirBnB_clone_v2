#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    def __init__(self, *args, **kwargs):
        """ Initializes State
        """
        super().__init__(*args, **kwargs)

    if env == "db":
        # DBstorage
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state', cascade="all, delete")
    else:
        # Filestorage
        # getter attribute cities that returns the list of City instances with
        # state_id equals to the current State.id
        #  It will be the FileStorage relationship between State and City
        @property
        def cities(self):
            state_cities_instance =[]
            all_cities = models.Storage.all(City)
            for one_city in all_cities:
                if one_city.state_id == State.id:
                    state_cities_instance.append(one_city)
            return state_cities_instance

