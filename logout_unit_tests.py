from unittest import TestCase
from Logout import Logout
from TextFileInterface import TextFileInterface
from User import User


class TestLogout(TestCase):
    def test_successful_logout(self):
        database = TextFileInterface()
        logout = Logout(database)
        user = logout.action(["logout"], User("testuser", "supervisor"))
        self.assertIsNone(user)

    def test_not_logged_on(self):
        database = TextFileInterface()
        logout = Logout(database)
        user = logout.action(["logout"], None)
        self.assertIsNone(user)

    def test_extra_args(self):
        database = TextFileInterface()
        logout = Logout(database)
        user = logout.action(["logout", "foo"], User("testuser", "supervisor"))
        self.assertIsNone(user)
