import Command


class CreateAccount(Command.Command):

    def __init__(self, environment):
        self.environment = environment
    """
        args is a list containing the following:
            ["create_account", "username", "password", "role"]
    """
    def action(self, args):
        if self.environment.user is None:
            self.environment.debug("You must be logged in to perform this action.")
            return

        if self.environment.user.get_role() not in ["supervisor", "administrator"]:
            self.environment.debug("Permission Denied")
            return

        if len(args) != 4:
            self.environment.debug("Invalid Arguments")
            return

        if self.get_user(args[2]) is not None:
            self.environment.debug("Username is already taken.")
            return

        if not self.is_valid_role(args[3]):
            self.environment.debug("Invalid Role")
            return

        self.environment.database.create_account(args[1], args[2], args[3])

        return "Account Created"


class DeleteAccount(Command.Command):
    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["delete_account", username]
    """
    def action(self, args):
        if self.environment.user is None:
            self.environment.debug("You must be logged in to perform this action.")
            return

        if self.environment.user.get_role() not in ["administrator", "supervisor"]:
            self.environment.debug("Permission denied")
            return

        if self.get_user(args[1]) is None:
            self.environment.debug("User to delete doesn't exist")
            return

        self.environment.database.delete_account(args[1])
        print("Account Deleted")
