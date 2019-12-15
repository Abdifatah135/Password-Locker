import unittest
import pyperclip
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """    
        Set up method to run before each test cases.
        """
        self.new_user = User(
            "Abdi", "Mohamed", "12345ke", "abdi@gmail.com")  # create user object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.first_name, "Abdi")
        self.assertEqual(self.new_user.last_name, "Mohamed")
        self.assertEqual(self.new_user.password_number, "12345ke")
        self.assertEqual(self.new_user.email, "abdi@gmail.com")

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

# setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []





    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "12345ke",
                               "test@user.com")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "12345ke",
                               "test@user.com")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by password number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test", "user", "112233tz",
                               "test@user.com")  # new user
        test_user.save_user()

        found_user = User.find_by_number("112233tz")

        self.assertEqual(found_user.email, test_user.email)
        
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","112233tz","test@user.com") # new contact
        test_user.save_user()

        user_exists = User.user_exist("112233tz")

        self.assertTrue(user_exists)
        
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)


if __name__ == '__main__':
    unittest.main()
