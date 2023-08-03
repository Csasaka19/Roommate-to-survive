#!/usr/bin/python3
from roommate_app import roommate_app

@roommate_app.route('/')
@roommate_app.route('/index')
def index():
    return "Hello, World!"