import Command


class AssignCourse(Command.Command):
    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["assign_Course", courseId, accountId]
    """
    def action(self, args):
        print("Assign Course command entered.")
        """
        Assigns a account to a specified course
        """


class CreateCourse(Command.Command):
    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["create_Course", course_number, course_name,]
    """
    def action(self, args):
        if self.environment.user is None:
            print("You must be logged in to perform this action.")
            return

        if self.environment.user.get_role() not in ["supervisor", "admin"]:
            print("Permission Denied")
            return

        if len(args) != 3:
            print("Invalid Arguments")
            return

        self.environment.database.create_course(args[1], args[2])

        print("Course Created Successfully")
        return
