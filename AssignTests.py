import unittest

class AssignTests(unittest.TestCase):

    def test_assign_ta(self):
        """
            When assign_ta command is entered, it takes two arguments:
            - TA Name
            - Class Number
            The response is a string, either:
            - Success: "Assigned {TA Name} to {Class Number}."
            - Failure: "Error assigning to class. {Explanation}."
        """

        # Command: "assign_ta apoorv 361", expect success
        self.assertEqual(command("assign_ta apoorv 361"), "Assigned apoorv to 361.")
        # Command: "assign_ta apoorv", expect failure (no class given)
        self.assertEqual(command("assign_ta apoorv"), "Error assigning to class. No class given.")
        # Command: "assign_ta", expect failure (no ta name given)
        self.assertEqual(command("assign_ta"), "Error assigning to class. No ta given.")
        # Command: "assign_ta andy 361", expect failure (not a TA)
        self.assertEqual(command("assign_ta andy 361"), "Error assigning to class. Not a TA")

    def test_assign_instructor(self):
        """
            When assign_instructor command is entered, it takes two arguments:
            - Instructor Name
            - Class Number
            The response is a string, either:
            - Success: "Assigned {Instructor Name} to {Class Number}."
            - Failure: "Error assigning to class. {Explanation}."
        """

        # Command: "assign_instructor jayson 361", expect success
        self.assertEqual(command("assign_instructor jayson 361"), "Assigned jayson to 361.")

    def test_assign_lab(self):
        """
            When assign_lab command is entered, it takes two arguments:
            - TA Name
            - Class Number
            - Lab Number
            The response is a string, either:
            - Success: "Assigned {TA Name} to {Class Number} lab {Lab Number}."
            - Failure: "Error assigning to Lab. {Explanation}."
        """

        # Command: "assign_lab apoorv 361", expect success
        self.assertEqual(command("assign_ta apoorv 361 801"), "Assigned apoorv to 361 lab 801.")
        # Command: "assign_lab apoorv", expect failure (no class given)
        self.assertEqual(command("assign_lab apoorv"), "Error assigning to lab. No class given.")
        # Command: "assign_lab", expect failure (no ta name given)
        self.assertEqual(command("assign_lab"), "Error assigning to lab. No ta given.")
        # Command: "assign_lab andy 361", expect failure (not a TA)
        self.assertEqual(command("assign_lab andy 361"), "Error assigning to lab. Not a TA")
