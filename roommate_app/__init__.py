#!/usr/bin/python3
'''This module defines the application object for the application'''
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Sets the name of the application to the name of the module
roommate_app = Flask(__name__)
# Configures the application based on the Config class in config.py
roommate_app.config.from_object(Config)
# Creates the database object for the application
roommate_db = SQLAlchemy(roommate_app)
# Creates the migration engine for the application for eventual database migrations
migrate = Migrate(roommate_app, roommate_db)

from roommate_app import routes, models
