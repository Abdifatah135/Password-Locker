import unittest

from credential import Credential

class TestCredential(unittest.TestCase):
    
    def setUp(self):
        """    
        Set up method to run before each test cases.
        """
        self.new_credential = Credential(
            "Twitter", "12345ke",)  # create credential object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.account_name, "Twitter")
        self.assertEqual(self.new_credential.password, "12345ke")
        
    def test_save_credential(self):
    
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

# setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []





    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple  credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test",  "12345ke",
                               )  # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a user from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test", "12345ke",
                               )  # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()  # Deleting a credential object
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by password number and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","112233tz",
                            )  # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_number("112233tz")

        self.assertEqual(found_credential.password, test_credential.password)
        
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","112233tz") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("112233tz")

        self.assertTrue(credential_exists)
        
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
        
   

if __name__ == '__main__':
    unittest.main()