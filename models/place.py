#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    def __init__(self, *args, **kwargs):
        """ Initializes Place
        """
        super().__init__(*args, **kwargs)

    if env == "db":
        # DBstorange
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'),  nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),  nullable=False)
        name = Column(String(60), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []
        reviews = relationship('Review', cascade='all, delete', backref='place')

    else:
        # filestorage
        # getter attribute reviews that returns the list
        # of Review instances with place_id getter attribute reviews
        # that returns the list of Review instances with place_id
        @property
        def reviews(self):
            places_reviews_instances = []
            all_reviews = models.storage.all(Review)
            for one_review in all_reviews:
                if one_review.place_id == Place.id:
                    places_reviews_instances.append(one_review)
            return places_reviews_instances

