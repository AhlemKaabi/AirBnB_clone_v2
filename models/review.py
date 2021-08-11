#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.sql.expression import null
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime, ForeignKey

class Review(BaseModel):
    """ Review classto store review information """
    def __init__(self, *args, **kwargs):
        """ Initializes Review
        """
        super().__init__(*args, **kwargs)

    if env == "db":
            # DBstorage
        __tablename__ = ' reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        # Filestorage
        place_id = ""
        user_id = ""
        text = ""


