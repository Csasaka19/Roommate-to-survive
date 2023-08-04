#!/usr/bin/python3
'''This module defines the configuration for the application'''''
import os
# Sets a variable based on the location of the config.py file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''This class defines the configuration for the application'''
    # Prevents cross-site request forgery attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-238394-incognito'
    # Sets the location of the database and its URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'roommate_app.db')
        # disables a feature in SQLAlchemy that signals the application(roommate_app) every time a change 
        # is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False