#!/usr/bin/python3
from roommate_app import roommate_app
from flask import render_template

@roommate_app.route('/')
@roommate_app.route('/index')
def index():
    return render_template('index.html', title='Home')