import Command


class CreateLab(Command.Command):
    def __init__(self, environment):
        self.environment = environment
    """
        args is a list containing the following:
            ["create_lab", course_number, lab_number]
    """
    def action(self, args):
        if self.environment.user is None:
            print("You must be logged in to perform this action.")
            return

        if self.environment.user.get_role() not in ["instructor", "supervisor", "admin"]:
            print("Permission Denied")
            return

        if len(args) != 3:
            print("Invalid Arguments")
            return
        course_num = args[1]
        lab_num = args[2]
        if not self.course_exists(course_num):
            print("Course does not exist")
            return

        if self.lab_exists(course_num, lab_num):
            print("Lab already exists")
            return
        self.environment.database.create_lab(course_num, lab_num)
        print("Lab created successfully")
        return


class AssignLab(Command.Command):

    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["assign_lab", course_number, lab_number, account_name]
    """
    def action(self, args):
        """
        Assigns a TA to a specified lab section
        """
        if self.environment.user is None:
            print("You must be logged in to perform this action.")
            return

        if self.environment.user.get_role() not in ["instructor", "supervisor", "admin"]:
            print("Permission Denied")
            return

        if len(args) != 4:
            print("Invalid Arguments")
            return
        course_num = args[1]
        lab_num = args[2]
        if not self.lab_exists(course_num, lab_num):
            print("Lab does not exist")
            return
        if self.lab_assigned(course_num, lab_num):
            print("Lab already assigned to a TA")
            return

        ta = self.get_user(args[3])
        if ta is None:
            print("Instructor for course does not exist")
            return

        if ta.get_role() != "TA":
            print("Instructor for course is not an instructor")
            return

        self.environment.database.set_lab_assignment(args[1], args[2], args[3])
        print("Lab assigned successfully")
        return
