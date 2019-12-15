class User:
    
    
    """
    Class that generates new instances of users.
    """
    user_list = [] # Empty user list
    
    def __init__(self, user_name, password,number,email):
        '''
        _  __init__ method that helps us define properties for our objects.
        '''
        self.user_name = user_name
        self.password = password
        self.phone_number = number
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
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            user_name: user_name to search for
        Returns :
            User of person that matches the user_name.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user
