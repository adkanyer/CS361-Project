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
        SUCCESS_MESSAGE = "Assigned to course."
        FAILURE_MESSAGE = "Error assigning to course."

        if self.environment.user is None:
            self.environment.debug("You must be logged in to perform this action.")
            return FAILURE_MESSAGE

        if self.environment.user.get_role() not in ["supervisor", "admin"]:
            self.environment.debug("Permission Denied")
            return FAILURE_MESSAGE

        if len(args) != 3:
            self.environment.debug("Invalid Arguments")
            return FAILURE_MESSAGE

        course_num = args[1]
        if not self.course_exists(course_num):
            self.environment.debug("Course does not exist")
            return FAILURE_MESSAGE
        if self.course_assigned(course_num):
            self.environment.debug("Course already assigned to instructor")
            return FAILURE_MESSAGE

        instructor = self.get_user(args[2])
        if instructor is None:
            self.environment.debug("Instructor for course does not exist")
            return FAILURE_MESSAGE

        if instructor.get_role() != "instructor":
            self.environment.debug("Instructor for course is not an instructor")
            return FAILURE_MESSAGE

        self.environment.database.set_course_assignment(args[1], args[2])
        self.environment.debug("Course assigned successfully")
        return SUCCESS_MESSAGE


class CreateCourse(Command.Command):
    def __init__(self, environment):
        self.environment = environment

    """
        args is a list containing the following:
            ["create_Course", course_number, course_name,]
    """
    def action(self, args):
        SUCCESS_MESSAGE = "Created course"
        FAILURE_MESSAGE = "Error creating course."

        if self.environment.user is None:
            self.environment.debug("You must be logged in to perform this action.")
            return FAILURE_MESSAGE

        if self.environment.user.get_role() not in ["supervisor", "admin"]:
            self.environment.debug("Permission Denied")
            return FAILURE_MESSAGE

        if len(args) != 3:
            self.environment.debug("Invalid Arguments")
            return FAILURE_MESSAGE

        self.environment.database.create_course(args[1], args[2])

        self.environment.debug("Course Created Successfully")
        return SUCCESS_MESSAGE


