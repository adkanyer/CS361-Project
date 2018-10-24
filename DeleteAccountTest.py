import unittest

class DeleteAccountTest(unittest.TestCase):
    def setUp(self):
        self.ui = UI()
        """
            create dummy account for each of the types of users:
            supervisor, administrator, instructor and TA and then
            log them in for their respected tests
            Each test is implemented by first creating and then deleting an account
        """
        self.ui.command("create_account userSupervisor password supervisor")
        self.ui.command("create_account userAdministrator password administrator")
        self.ui.command("create_account userInstructor password instructor")
        self.ui.command("create_account userTA password ta")

        """
            The supervisor and administrator are able to delete accounts
            when delete_account command is entered, it expects 1 arguments:
            - username
            The response is a string of either:
            - "Account Deleted" if successful
            - "Unable to delete account" if unsuccessful
    """

    def test_command_delete_account_supervisor(self):

        # login as supervisor
        self.ui.command("login userSupervisor password")
        self.ui.command("create_account john password ta")
        self.assertEquals("delete_account john", "Account Deleted")

    def test_command_delete_account_administrator(self):

        # login as administrator
        self.ui.command("login userAdministrator password")
        self.ui.command("create_account adam password supervisor")
        self.assertEquals("delete_account adam", "Account Deleted")

    def test_command_delete_account_instructor(self):

        self.ui.command("login userAdministrator password")
        self.ui.command("create_account aaron password supervisor")
        self.ui.commmand("logout")

        # login as instructor
        self.ui.command("login userInstructor password")
        # instructor cannot delete accounts
        self.assertEquals("delete_account aaron", "Unable to delete account")

    def test_command_delete_account_TA(self):
        self.ui.command("login userSupervisor password")
        self.ui.command("create_account tim@uwm.edu tim password")
        self.ui.command("logout")

        # login as TA
        self.ui.command("login TA password")
        # TA cannot delete accounts
        self.assertEquals("delete_account tim", "Unable to delete account")

    def test_command_delete_account_format(self):
        # login as administrator
        self.ui.command("login userAdministrator password")
        # not enough arguments
        self.assertEquals("delete_account", "Unable to delete_account")

    def test_command_delete_account_nonexisting(self):
        # login as supervisor
        self.ui.command("login userSupervisor password")
        self.assertEquals("delete_account noUser", "Unable to delete account")