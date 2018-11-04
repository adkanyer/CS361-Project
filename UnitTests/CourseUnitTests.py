import unittest
from TextFileInterface import TextFileInterface
from Components.CourseCommands import CreateCourse, AssignCourse
from Environment import Environment
from User import User


class CreateCourseUnitTests(unittest.TestCase):

    def setUp(self):
        tfi = TextFileInterface(relative_directory="TestDB/")
        self.environment = Environment(tfi)
        self.environment.database.clear_database()

    def test_create_course_correct_args(self):
        self.environment.user = User("root", "supervisor")
        create_course = CreateCourse(self.environment)
        response = create_course.action(["create_course", "1", "course1"])

        self.assertTrue(create_course.course_exists("1"))
        self.assertEqual(response, "Created course.")

        self.environment.user = User("subroot", "administrator")
        create_course = CreateCourse(self.environment)
        response = create_course.action(["create_course", "2", "course2"])

        self.assertTrue(create_course.course_exists("2"))
        self.assertEqual(response, "Created course.")

    def test_create_course_no_permissions(self):
        self.environment.user = User("instructor_acct", "instructor")

        create_course = CreateCourse(self.environment)
        response = create_course.action(["create_course", "1", "course1"])

        self.assertFalse(create_course.course_exists("1"))
        self.assertEqual(response, "Error creating course.")

        self.environment.user = User("ta_acct", "TA")

        create_course = CreateCourse(self.environment)
        response = create_course.action(["create_course", "2", "course2"])

        self.assertFalse(create_course.course_exists("2"))
        self.assertEqual(response, "Error creating course.")

    def test_create_course_not_logged_in(self):
        create_course = CreateCourse(self.environment)
        response = create_course.action(["create_course", "1", "course1"])

        self.assertFalse(create_course.course_exists("1"))
        self.assertEqual(response, "Error creating course.")

    def test_create_course_course_exists(self):
        self.environment.user = User("root", "supervisor")
        self.environment.database.create_course("1", "course1")

        create_course = CreateCourse(self.environment)
        response = create_course.action(["create_course", "1", "course1"])

        self.assertEqual(response, "Error creating course.")

