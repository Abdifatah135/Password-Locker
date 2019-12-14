class User:
    
    
    """
    Class that generates new instances of users.
    """
    user_list = [] # Empty user list
    
    def __init__(self, user_name, password):
        '''
        _  __init__ method that helps us define properties for our objects.
        '''
        self.user_name = user_name
        self.password = password
        
    # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
