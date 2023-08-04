#!/usr/bin/env python
'''This module defines database models for the application'''
from roommate_app import roommate_db
from datetime import datetime


class User(roommate_db.Model):
    '''This class defines the user model for the application'''
    __tablename__ = 'user'
    id = roommate_db.Column(roommate_db.Integer, primary_key=True, autoincrement=True)
    username = roommate_db.Column(roommate_db.String(64), index=True, unique=True)
    email = roommate_db.Column(roommate_db.String(120), index=True, unique=True)
    password_hash = roommate_db.Column(roommate_db.String(128))
    age = roommate_db.Column(roommate_db.Integer, index=True)
    phone = roommate_db.Column(roommate_db.String(10), index=True)
    country = roommate_db.Column(roommate_db.String(20), index=True)
    gender = roommate_db.Column(roommate_db.String(10), index=True)
    budget = roommate_db.Column(roommate_db.Integer, index=True)
    
    def __repr__(self):
        '''This method returns a string representation of the user model'''
        return '<User {} : Country {}>'.format(self.username, self.country)