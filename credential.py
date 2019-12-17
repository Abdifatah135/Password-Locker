class Credential:
    
    """
    Class that generates new instances of users.
    """
    credential_list = [] # Empty credential list
    
    def __init__(self, account_name, password):
        
        self.account_name = account_name
        self.password = password
        
    def save_credential(self):
    
        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)
        
    def delete_credential(self):
    
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
        
    @classmethod
    def find_by_number(cls,password):
        '''
        Method that takes in a password and returns a credential that matches that password.

        Args:
            password: password to search for
        Returns :
            Credential of person that matches the password.
        '''

        for credential in cls.credential_list:
            if credential.password == password:
                return credential
            
    @classmethod
    def credential_exist(cls,password):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            number: password number to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credential in cls.credential_list:
            if credential.password == password:
                    return True

        return False
    
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
    
    