import unittest

class AssignTests(unittest.TestCase):

    def setup(self):
        self.ui.command("create_account Supervisor SupervisorPassword supervisor")
        self.ui.command("create_account Administrator AdministratorPassword administrator")
        self.ui.command("create_account Instructor InstructorPassword instructor")
        self.ui.command("create_account TA TAPassword ta")
    """
        When assign_ta command is entered, it takes two arguments:
        - TA Name
        - Class Number
        The response is a string, either:
        - Success: "Assigned to class."
        - Failure: "Error assigning to class."
    """
    def test_assign_ta_by_supervisor_success(self):
        # Command: "assign_ta apoorv 361", expect success
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_ta TA 361"), "Assigned to class")

    def test_assign_ta_by_administrator_fail(self):
        # Command: "assign_ta TA 361", expect success
        self.ui.command("login Administrator AdministratorPassword")
        self.assertEqual(self.ui.command("assign_ta TA 361"), "Error assigning to class")

    def test_assign_ta_by_ta_fail(self):
        # Command: "assign_ta TA 361", expect success
        self.ui.command("login TA TAPassword")
        self.assertEqual(self.ui.command("assign_ta TA 361"), "Error assigning to class")

    def test_assign_ta_no_class_given(self):
        # Command: "assign_ta TA", expect failure (no class given)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_ta TA"), "Error assigning to class.")

    def test_assign_ta_no_args(self):
        # Command: "assign_ta", expect failure (no ta name given)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_ta"), "Error assigning to class.")

    def test_assign_ta_not_a_ta(self):
        # Command: "assign_ta Instructor 361", expect failure (not a TA)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_ta Instructor 361"), "Error assigning to class.")

    """
        When assign_instructor command is entered, it takes two arguments:
        - Instructor Name
        - Class Number
        The response is a string, either:
        - Success: "Assigned to class."
        - Failure: "Error assigning to class."
    """
    def test_assign_instructor_by_supervisor(self):
        # Command: "assign_instructor Instructor 361", expect success
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor 361"), "Assigned to class.")

    def test_assign_instructor_by_instructor(self):
        # Command: "assign_instructor Instructor 361", expect failure
        self.ui.command("login Instructor InstructorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor 361"), "Error assigning to class.")

    def test_assign_instructor_by_ta(self):
        # Command: "assign_instructor Instructor 361", expect failure
        self.ui.command("login TA TAPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor 361"), "Error assigning to class.")

    def test_assign_instructor_not_instructor(self):
        # Command: "assign_instructor TA 361", expect error (not an instructor)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor TA 361"), "Error assigning to class.")

    def test_assign_instructor_no_class(self):
        # Command: "assign_instructor jayson", expect error (no class given)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor"), "Error assigning to class.")

    def test_assign_instructor_no_args(self):
        # Command: "assign_instructor", expect error (no instructor given)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor"), "Error assigning to class.")

    """
        When assign_lab command is entered, it takes two arguments:
        - TA Name
        - Class Number
        - Lab Number
        The response is a string, either:
        - Success: "Assigned to lab."
        - Failure: "Error assigning to Lab."
    """
    def test_assign_lab(self):
        # Command: "assign_lab TA 361", expect success
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_ta TA 361 801"), "Assigned to class.")

    def test_assign_lab_no_class(self):
        # Command: "assign_lab TA", expect failure (no class given)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_lab TA"), "Error assigning to lab.")

    def test_assign_lab_no_args(self):
        # Command: "assign_lab", expect failure (no ta name given)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_lab"), "Error assigning to lab.")


    def test_assign_lab_not_ta(self):
        # Command: "assign_lab Instructor 361", expect failure (not a TA)
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_lab Instructor 361"), "Error assigning to lab.")

    """
        When view_instructor_assignments command is entered, it takes no arguments
        The response is a string with a line for each course in format
            "{Course Number} {Course Name} {Instructor Name}"
        Fail if the logged in user does not have permission:
            "Error viewing instructor assignments."
    """
    def view_instructor_assignments_by_supervisor(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEquals(self.ui.command("view_instructor_assignments"),
                          "361 SystemsProgramming Instructor")

    def view_instructor_assignments_by_administrator(self):
        self.ui.command("login Administrator AdministratorPassword")
        self.assertEquals(self.ui.command("view_instructor_assignments"),
                          "361 SystemsProgramming Instructor")

    def view_instructor_assignments_by_instructor(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEquals(self.ui.command("view_instructor_assignments"),
                          "Error viewing instructor assignments.")

    def view_instructor_assignments_by_ta(self):
        self.ui.command("login TA TAPassword")
        self.assertEquals(self.ui.command("view_instructor_assignments"),
                          "Error viewing instructor assignments.")

    """
        When view_ta_assignments command is entered, it takes no arguments
        The response is a string with a line for each course in format
            "{Course Number} {Course Name} lab {Lab Number} {TA Name}"
        Fail if logged in user does not have permissions:
            "Error viewing ta assignments."
    """
    def view_ta_assignments_by_supervisor(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEquals(self.ui.command("view_ta_assignments"),
                          "361 SystemsProgramming lab 801 TA")

    def view_ta_assignments_by_administrator(self):
        self.ui.command("login Administrator AdministratorPassword")
        self.assertEquals(self.ui.command("view_ta_assignments"),
                          "361 SystemsProgramming lab 801 TA")

    def view_ta_assignments_by_instructor(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEquals(self.ui.command("view_ta_assignments"),
                          "361 SystemsProgramming lab 801 TA")

    def view_ta_assignments_by_ta(self):
        self.ui.command("login TA TAPassword")
        self.assertEquals(self.ui.command("view_ta_assignments"),
                          "361 SystemsProgramming lab 801 TA")
