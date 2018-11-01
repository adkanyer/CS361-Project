import TextFileInterface
import User
import hashlib

class Login:

    def __init__(self, database):
        self.database = database

    """
        args is a list containing the following:
            ["login", <username>, <password>]
    """
    def action(self, args, user):
        if user is not None:
            print("Someone else is logged in.")
            return user

        user_list = self.database.get_accounts()

        for i in user_list:
            if i["name"] is args[1]:
                user = i

        hash = hashlib.new("md5")
        hash.update(b"args[2]")
        hashed_password = hash.hexdigest()
        if user["password"] != hashed_password:
            print("User name or Password is Incorrect")
            return None

        self.database.set_logged_in(user["username"])
        print("Logged in successfully")
        return User.User(user["username"], user["role"])
