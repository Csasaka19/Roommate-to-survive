#!/usr/bin/python3
"""This is the database storage and management module"""
import models
from models import user_profile
from models import booking
from models import review
from models import room_listing
from models import roommate_listing
from models import location
from models import dwelling_type
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlaclchemy.ext.declarative import declarative_base
from os import getenv

Base = declarative_base()

class Database_Storage():
    '''Database storage and class'''
    
    def __init__(self):
        """Initialize the database storage engine"""
        user = getenv("ROOMMATE_MYSQL_USER")
        passwd = getenv("ROOMMATE_MYSQL_PWD")
        db = getenv("ROOMMATE_MYSQL_DB")
        host = getenv("ROOMMATE_MYSQL_HOST")
        env = getenv("ROOMMATE_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = self.__Session()
    
    def delete(self, obj=None):
        """Delete an object from the database"""
        if obj is not None:
            self.__session.delete(obj)
            
    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()
        
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
        
    def close(self):
        """Close the current database session"""
        self.__session.close()
        
    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
    