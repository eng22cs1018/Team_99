import unittest
from utils.auth import create_user, validate_user

class TestAuthModule(unittest.TestCase):
    def setUp(self):
        self.test_user = "testuser"
        self.test_pass = "Test@123"

    def test_user_creation(self):
        self.assertTrue(create_user(self.test_user, self.test_pass))
        self.assertFalse(create_user(self.test_user, self.test_pass))  # Duplicate

    def test_valid_login(self):
        self.assertTrue(validate_user(self.test_user, self.test_pass))

    def test_invalid_login(self):
        self.assertFalse(validate_user(self.test_user, "wrongpass"))

if __name__ == "__main__":
    unittest.main()