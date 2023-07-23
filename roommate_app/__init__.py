#!/usr/bin/python3
from flask import Flask
from config import Config

roommate_app = Flask(__name__)
roommate_app.config.from_object(Config)

from roommate_app import routes
