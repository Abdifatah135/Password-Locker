#!/usr/bin/env python3.6
from user import User

def create_contact(fname,lname,password,email):
    '''
    Function to create a new user
    '''
    new_contact = User(fname,lname,password,email)
    return new_user