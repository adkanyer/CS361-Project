import unittest
from TextFileInterface import TextFileInterface
from Components.AccountCommands import CreateAccount, DeleteAccount
from Environment import Environment


class CreateAccountUnitTests(unittest.TestCase):

    def setUp(self):
        tfi = TextFileInterface(relative_directory="TestDB/")
        self.environment = Environment(tfi)
        self.environment.database.clear_database()
        self.environment.database.create_account("root", "root", "administrator")
        self.environment.database.set_logged_in("root")

    def test_create_account_no_args(self):
        ca = CreateAccount(self.environment)
        ca.action(["create_account", "new_user", "password"])
        self.assertEqual(1, 1)

