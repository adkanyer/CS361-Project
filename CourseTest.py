import unittest

class CourseTests(unittest.TestCase):

    def test_command_create_course(self):
        """
            When create_course command is entered, it expects two arguments:
             - class number
             - class name
            The response is a string, either:
             - If Successful: "Created course."
             - If Failure: "Error creating course."
        """

        # Command: "create_course 361 SystemsProgramming", expect success
        self.assertEquals(command("create_course 361 SystemsProgramming"), "Created course.")
        # Command: "create_course 361 SystemsProgramming", expect error, duplicate course
        self.assertEquals(command("create_course 361 SystemsProgramming"), "Error creating course.")
        # Command: "create_course", expect error, not enough arguments
        self.assertEquals(command("create_course"), "Error creating account.")

    def test_command_delete_course(self):
        """
            When delete_course command is entered, it expects one argument:
                - course number
            The response is a string, either:
                - Success: "Deleted course."
                - Failure: "Error deleting course."
        """

        # Command: "delete_course 361", expect success
        self.assertEqual(command("delete_course 361"), "Deleted course.")

        # Command: "delete_course 417", expect failure (course not found)
        self.assertEqual(command("delete_course 417"), "Error deleting course.")

        # Command: "delete_course", expect failure
        self.assertEqual(command("delete_course"), "Error deleting course.")

