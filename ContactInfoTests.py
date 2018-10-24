import unittest


class ContactInfoTests(unittest.TestCase):
    def setUp(self):
        self.ui = UI()

    def test_command_view_public_info(self):
        """
            Only public information is available for a normal user to see. Only those with permission can view
            private information like address and phone number.

            When view_info command is entered for a user you only have public access to, it expects one argument:
            - username

            The response is a string:
            - If successful: "Username: user, Email: email"
            - If failure: "Username does not exist"
        """
        # Create a TA account and log in as part of the setup
       # self.ui.command("create_account userTA userPassword TA")
       # self.ui.command("login userTA userPassword")

        # view own contact info, expect success
        self.assertEquals(self.ui.command("view_info"), "Username: erin, Email: erinfink@uwm.edu, Phone number: 1231231234, "
                                                "Address: 2311 E Hartford Ave Milwaukee, WI 53211")
        # Command: "view_info user", expect success
        self.assertEquals(self.ui.command("view_info Erin"), "Username: erin, Email: erinfink@uwm.edu")

        # Command: "view_info fake", expect success
        self.assertEquals(self.ui.command("view_info fake"), "Username does not exist.")

    def test_command_Instructor_change_contact_info(self):
