#!/usr/bin/python3
'''This module defines routes for the application'''
from roommate_app import roommate_app
from flask import render_template, url_for, flash, redirect
from roommate_app.forms import LoginForm

@roommate_app.route('/')
@roommate_app.route('/index')
def index():
    '''This function defines the index route for the application'''
    return render_template('index.html', title='Home')

@roommate_app.route('/login', methods=['GET', 'POST'])
def login():
    '''This function defines the login route for the application'''
    form = LoginForm()
    if form.validate_on_submit(): # returns True if the browser sends a POST request
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Log in', form=form)