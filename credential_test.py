import unittest

from credential import Credential

class TestCredential(unittest.TestCase):
    
    def setUp(self):
        """    
        Set up method to run before each test cases.
        """
        self.new_credential = Credential(
            "Abdi", "12345ke",)  # create credential object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.account_name, "Abdi")
        self.assertEqual(self.new_credential.password, "123245ke")