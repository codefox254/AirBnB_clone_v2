#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage

class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        """Returns the list of City objects linked to the current State"""
        city_list = []
        all_cities = storage.all("City").values()
        for city in all_cities:
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

