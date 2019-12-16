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

def main():
    
    print("Hello Welcome to your contact list. What is your name?")
            
    fisrt_name = input()

    print(f"Hello {fisrt_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cu - create a new user, du - display users, fu -find a user, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Password ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()
                            
                            save_users(create_contact(f_name,l_name,p_number,e_address)) # create and save new user.
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.password_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == 'fu':

                            print("Enter the number you want to search for")

                            search_password = input()
                            if check_existing_users(search_password):
                                    search_user = find_user(search_password)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_user.password_number}")
                                    print(f"Email address.......{search_user.email}")
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    
    main()