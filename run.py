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
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_by_number(password)

def check_existing_users(password):
    '''
    Function that check if a user exists with that password and return a Boolean
    '''
    return User.user_exist(password)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
