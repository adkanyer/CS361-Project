import unittest
from TextFileInterface import TextFileInterface
from Components.AccountCommands import CreateAccount, DeleteAccount
from Environment import Environment


class CreateAccountUnitTests(unittest.TestCase):

    def setUp(self):
        self.environment = Environment(TextFileInterface())

    def test_create_account_no_args(self):
        ca = CreateAccount(self.environment)
        self.assertEqual(1, 1)

