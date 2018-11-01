import Command


class CreateCourse(Command.Command):
    def __init__(self):
        pass

    """
    TestCommit
        args is a list containing the following:
            ["create_Course", name, instructor, tas, assignments]
    """
    def action(self, args):
        print("Create Course command entered.")
