import User
import hashlib
import Command


class Login(Command.Command):

    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["login", <username>, <password>]
    """
    def action(self, args):
        if self.environment.user is not None:
            print("Someone else is logged in.")
            return

        if len(args) != 3:
            print("Username or Password is Incorrect")
            return

        user_list = self.environment.database.get_accounts()

        account = {}

        for i in user_list:
            if i["name"] == args[1]:
                account = i

        if len(account) == 0:
            print("Username or Password is Incorrect")
            return

        h = hashlib.new("md5")
        entered_password = args[2].rstrip()
        h.update(f"{entered_password}".encode("ascii"))
        hashed_password = h.hexdigest()

        if account["password"] != hashed_password:
            print("User name or Password is Incorrect")
            return

        self.environment.database.set_logged_in(account["name"])
        self.environment.user = User.User(account["name"], account["role"])
        print("Logged in successfully")
        return
