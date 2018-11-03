from unittest import TestCase
from Login import Login
from TextFileInterface import TextFileInterface
from User import User


class Login_Unit_Tests(TestCase):

    def test_not_enough_args(self):
        database = TextFileInterface()
        login = Login(database)
        user = login.action(["login", "testuser"], None)
        self.assertIsNone(user)

    def test_too_many_args(self):
        database = TextFileInterface()
        login = Login(database)
        user = login.action(["login", "testuser", "1234", "foo"], None)
        self.assertIsNone(user)

    def test_already_logged_in(self):
        database = TextFileInterface()
        database.create_account("testuser", "1234", "supervisor")
        login = Login(database)
        user = login.action(["login", "testuser", "1234", "foo"], User("test", "role"))
        self.assertIsNotNone(user)

    def test_wrong_username(self):
        database = TextFileInterface()
        database.create_account("testuser", "1234", "supervisor")
        login = Login(database)
        user = login.action(["login", "testuse", "1234"], None)
        self.assertIsNone(user)

    def test_wrong_password(self):
        database = TextFileInterface()
        database.create_account("testuser", "1234", "supervisor")
        login = Login(database)
        user = login.action(["login", "testuser", "4321"], None)
        self.assertIsNone(user)

    def test_wrong_both(self):
        database = TextFileInterface()
        database.create_account("testuser", "1234", "supervisor")
        login = Login(database)
        user = login.action(["login", "testuse", "123"], None)
        self.assertIsNone(user)

    def test_all_correct(self):
        database = TextFileInterface()
        database.create_account("testuser", "1234", "supervisor")
        login = Login(database)
        user = login.action(["login", "testuser", "1234"], None)
        self.assertIsNotNone(user)
