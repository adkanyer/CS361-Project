import Command


class CreateCourse(Command.Command):
    def __init__(self, database):
        self.database = database

    """
        args is a list containing the following:
            ["create_Course", course_number, course_name,]
    """
    def action(self, args, user):
        if user is None:
            print("You must be logged in to perform this action.")
            return None

        if user.get_role() not in ["supervisor", "admin"]:
            print("Permission Denied")
            return user

        if len(args) != 2:
            print("Invalid Arguments")
            return user

        self.database.create_course(args[1], args[2],)

        print("Course Created Successfully")
        return None


