#!/usr/bin/env python3.6
from user import User

def create_contact(fname,lname,password,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,password,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()