#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """
        Amenity class
    """
    def __init__(self, *args, **kwargs):
        """
            Initializes User
        """
        super().__init__(*args, **kwargs)
    if env == "db":
        __tablename__ == 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = Table('place_amenity', Base.metadata,
                                Column('place_id',  String(60), ForeignKey('places.id')),
                                Column('amenity_id', String(60), ForeignKey('right.id')))
