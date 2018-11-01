import Command


class AssignCourse(Command.Command):
    def __init__(self):
        pass

    """
        args is a list containing the following:
            ["assign_Course", courseId, accountId]
    """
    def action(self, args):
        print("Assign Course command entered.")
