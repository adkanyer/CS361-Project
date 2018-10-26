import Login
import Logout
import CreateAccount
import DeleteAccount


class UI(object):
    # instantiate and instance of each command type
    login = Login.Login()
    logout = Logout.Logout()
    create_account = CreateAccount.CreateAccount()
    delete_account = DeleteAccount.DeleteAccount()

    # dictionary matching strings to commands
    commands = {
        "login": login,
        "logout": logout,
        "create_account": create_account,
        "delete_account": delete_account
    }

    def __init__(self):
        pass

    """
         string: input of type str
         attempts to initiate an action from
         one of the defined commands
    """
    def command(self, string):
        # parse input into a list, splitting by strings
        args = self.parse_commands(string)

        # get valid inputs that map to commands
        valid_args = self.commands.keys()

        # if command is valid initiate its action
        if args[0] in valid_args:
            self.commands[args[0]].action(args)
        else:
            print("Invalid Command")

    # input: command of type string
    # return: list of command separated by spaces
    @staticmethod
    def parse_commands(command):
        return command.split()
