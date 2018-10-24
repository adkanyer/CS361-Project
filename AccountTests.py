import unittest

class AccountTests(unittest.TestCase):

    # when create account is entered, a string
    # is returned indicating the account has been
    # created, prompting for more info or an error message.
    def test_command_create_account(self):
        #input: create account tyler 1234
        self.assertEquals(command("create_account tyler 1234 john3885@uwm.edu"),"Account has been created.")

     def test_command_create_account_duplicate(self):
        #no account created when input is bad.
        #input: create account tyler 1234 (duplicate username)
        self.assertEquals(command("create_account tyler 1234 john3885@uwm.edu"), "Error creating account.")

        # username not entered in command.
        # no account created
        self.assertEquals(command("create_account"), "Error creating account.")

        #password not entered with command
        #input: create account andy
        self.assertEquals(command("create_account andy"), "Password: ")

        #email not entered
        #input: create account
        self.assertEquals(command("create_account kyle 1234"), "Email: ")

    def test_command_edit_account(self):

        #command edit account prompts for username of account to edit
        self.assertEquals(command("edit_account"), "username: ")

        #command edit account followed by username
        self.assertEquals(command("edit_account tyler"), "What do you want to change: 'username', 'password', 'email' ? ")

        #edit your own account if logged in as user only command given.
        self.assertEquals(command("edit_account username"), "New Username: ")
        self.assertEquals(command("edit_account password"), "Enter Old Password: ")
        self.assertEquals(command("edit_account email"), "Enter New Email: ")
        self.assertEquals(command("edit_account phone"), "Enter New Phone Number: ")
        self.assertEquals(command("edit_account address"), "Enter New Address: ")

        #edit your own account if logged in as user single command.
        self.assertEquals(command("edit_account username Tyler"), "Username set to Tyler ")
        self.assertEquals(command("edit_account email john1234@uwm.edu"), "Email changed to john1234@uwm.edu")
        self.assertEquals(command("edit_account phone 6086321486"), "Phone number changed to 6086321486")
        self.assertEquals(command("edit_account address 2311 E Hartford Ave Milwaukee, WI 53211"),
                          "Address set to 2311 E Hartford Ave Milwaukee, WI 53211")


    def test_command_delete_account(self):

        #input delete account
        self.assertEquals(command("delete_account"), "Username: ")

        #input delete account tyler:
        #prompt to ensure they want to delete account
        #maybe have another prompt for the password as this should be a secure operation
        self.assertEquals(command("delete_account tyler"), "Are you sure you want to delete the account for tyler?")

        #code to make it to final password phase
        self.assertEquals(command("1234"), "Account has been deleted.")

    def test_command_view_account(self):

        #view own contact info
        self.assertEquals(command("view_info"), "Username: tyler, Email: john3885@uwm.edu, Phone number: 6086321486, "
                          "Address: 2311 E Hartford Ave Milwaukee, WI 53211")

        #view someone else's contact info : view_info username
        self.assertEquals(command("view_info tyler"), "Username: tyler, Email: john3885@uwm.edu, Phone number: 6086321486, "
                                                "Address: 2311 E Hartford Ave Milwaukee, WI 53211")

        #view invalid account
        self.assertEquals(command("view_info fakeaccount"), "Username does not exist.")
