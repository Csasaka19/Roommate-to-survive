#!/usr/bin/python3
'''This module defines the application object for the application'''
from roommate_app import roommate_app, roommate_db
from roommate_app.models import User, Review, Booking


# This decorator registers a function to be executed right before the application receives a request
@roommate_app.shell_context_processor
# This function returns a dictionary of items to be imported when the shell starts up
# Run the following command in the terminal to start the shell: $ flask shell
def make_shell_context():
    '''This function creates a shell context for the application'''
    return {'db': roommate_db, 'User': User, 'Review': Review, 'Booking': Booking}
