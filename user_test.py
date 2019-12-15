import unittest # Importing the unittest module
from user import User #importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","0712345678","james@ms.com") # create user object
        
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.password,"Muriuki")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"james@ms.com")

        
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
        
        
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
        
        
    def test_save_multiple_user(self):
        
        
        self.new_user.save_user()
        test_user = User("Test", "user","0712345678","test@user.com")  # user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
        
        
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user","0712345678","test@user.com")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)
        
        
    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by user_name and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com") # new user
        test_user.save_user()

        found_user = User.find_by_number("0712345678")

        


if __name__ == '__main__':
    unittest.main()