#!/usr/bin/python3
"""This module defines a class to manage DBstorage for hbnb clone"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import inspect
import os
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class DBStorage:
    """This class manages storage with MySQL DB"""
    __engine = None
    __session = None

    classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """ constructor for DBStorage """
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        d = {}
        if cls == None:
            for kls in self.classes:
                for obj in self.__session.query(eval(kls)).all():
                    key = str(kls) + '.' + obj.id
                    d[key] = obj
        else:
            objs = self.__session.query(cls)
            for obj in objs:
                key = str(cls) + '.' + obj.id
                d[key] = obj
        return d

    def new(self, obj):
        """ add object to the current database session """
        print(self.__session)
        print(obj)
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session