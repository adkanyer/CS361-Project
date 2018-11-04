import Command


class AssignCourse(Command.Command):
    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["assign_Course", course_number, account_name]
    """
    def action(self, args):
        """
        Assigns a account to a specified course
        """
        if self.environment.user is None:
            print("You must be logged in to perform this action.")
            return

        if self.environment.user.get_role() not in ["supervisor", "admin"]:
            print("Permission Denied")
            return

        if len(args) != 3:
            print("Invalid Arguments")
            return

        course_num = args[1]
        if not self.course_exists(course_num):
            print("Course does not exist")
            return
        if self.course_assigned(course_num):
            print("Course already assigned to instructor")
            return

        instructor = self.get_user(args[2])
        if instructor is None:
            print("Instructor for course does not exist")
            return

        if instructor.get_role() != "instructor":
            print("Instructor for course is not an instructor")
            return

        self.environment.database.set_course_assignment(args[1], args[2])
        print("Course assigned successfully")
        return


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


