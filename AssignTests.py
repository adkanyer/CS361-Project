import unittest

class AssignTests(unittest.TestCase):

    def test_assign_ta(self):
        """
            When assign_ta command is entered, it takes two arguments:
            - TA Name
            - Class Number
            The response is a string, either:
            - Success: "Assigned to class."
            - Failure: "Error assigning to class."
        """

        # Command: "assign_ta apoorv 361", expect success
        self.assertEqual(command("assign_ta apoorv 361"), "Assigned to class")
        # Command: "assign_ta apoorv", expect failure (no class given)
        self.assertEqual(command("assign_ta apoorv"), "Error assigning to class.")
        # Command: "assign_ta", expect failure (no ta name given)
        self.assertEqual(command("assign_ta"), "Error assigning to class.")
        # Command: "assign_ta andy 361", expect failure (not a TA)
        self.assertEqual(command("assign_ta andy 361"), "Error assigning to class.")

    def test_assign_instructor(self):
        """
            When assign_instructor command is entered, it takes two arguments:
            - Instructor Name
            - Class Number
            The response is a string, either:
            - Success: "Assigned to class."
            - Failure: "Error assigning to class."
        """

        # Command: "assign_instructor jayson 361", expect success
        self.assertEqual(command("assign_instructor jayson 361"), "Assigned to class.")

        # Command: "assign_instructor andy 361", expect error (not an instructor)
        self.assertEqual(command("assign_instructor andy 361"), "Error assigning to class.")

        # Command: "assign_instructor jayson", expect error (no class given)
        self.assertEqual(command("assign_instructor jayson"), "Error assigning to class.")

        # Command: "assign_instructor", expect error (no instructor given)
        self.assertEqual(command("assign_instructor"), "Error assigning to class.")

    def test_assign_lab(self):
        """
            When assign_lab command is entered, it takes two arguments:
            - TA Name
            - Class Number
            - Lab Number
            The response is a string, either:
            - Success: "Assigned to lab."
            - Failure: "Error assigning to Lab."
        """

        # Command: "assign_lab apoorv 361", expect success
        self.assertEqual(command("assign_ta apoorv 361 801"), "Assigned to class.")
        # Command: "assign_lab apoorv", expect failure (no class given)
        self.assertEqual(command("assign_lab apoorv"), "Error assigning to lab.")
        # Command: "assign_lab", expect failure (no ta name given)
        self.assertEqual(command("assign_lab"), "Error assigning to lab.")
        # Command: "assign_lab andy 361", expect failure (not a TA)
        self.assertEqual(command("assign_lab andy 361"), "Error assigning to lab.")

    def view_instructor_assignments(self):
        """
            When view_instructor_assignments command is entered, it takes no arguments
            The response is a string with a line for each course in format
                "{Course Number} {Course Name} {Instructor Name}"
        """
        self.assertEquals(command("view_instructor_assignments"),
                          "361 SystemsProgramming jayson")

    def view_ta_assignments(self):
        """
            When view_ta_assignments command is entered, it takes no arguments
            The response is a string with a line for each course in format
                "{Course Number} {Course Name} lab {Lab Number} {TA Name}"

        """
        self.assertEquals(command("view_ta_assignments"),
                          "361 SystemsProgramming lab 801 apoorv")
