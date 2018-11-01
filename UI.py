import Login
import Logout
import CreateAccount
import DeleteAccount
import CreateCourse
import AssignCourse


class UI(object):
    
    # dictionary matching strings to commands
    commands = {
        "login": Login.Login(),
        "logout": Logout.Logout(),
        "create_account": CreateAccount.CreateAccount(),
        "delete_account": DeleteAccount.DeleteAccount(),
        "create_course": CreateCourse.CreateCourse(),
        "assign_course": AssignCourse.AssignCourse()
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
