import TextFileInterface
import Command


class Logout(Command.Command):
    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
           ["logout"]
    """
    def action(self, args):
        if self.environment.user is None:
            print("No user is logged in.")
            return

        self.environment.database.set_logged_out()
        self.environment.user = None
        print("Logout Successful.")
        return
