import TextFileInterface
import Command


class Logout(Command.Command):
    def __init__(self, database):
        self.database = database

    """
        args is a list containing the following:
           ["logout"]
    """
    def action(self, args, user):
        if user is None:
            print("No user is logged in.")
            return None

        self.database.set_logged_out()
        print("Logout Successful.")
        return None
