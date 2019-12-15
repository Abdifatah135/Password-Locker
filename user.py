class User:
    
    
    """
    Class that generates new instances of users.
    """
    user_list = [] # Empty user list
    
    def __init__(self, first_name, last_name, password, email):
        
        self.first_name = first_name
        self.last_name = last_name
        self.password_number = password
        self.email = email
        
    # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
        
    def delete_user(self):
    
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
        
    @classmethod
    def find_by_number(cls,password):
        '''
        Method that takes in a password and returns a user that matches that number.

        Args:
            password: password_number to search for
        Returns :
            User of person that matches the number.
        '''

        for user in cls.user_list:
            if user.password_number == password:
                return user
            
    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.password_number == password:
                    return True

        return False
