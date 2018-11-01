import Command


class CreateAccount(Command.Command):
    def __init__(self):
        pass

    """
        args is a list containing the following:
            ["create_account", username, password, role]
    """
    def action(self, args):
        print("Create account command entered.")
