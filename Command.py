import abc
import User



class Command(abc.ABC):

    @abc.abstractmethod
    def action(self, args):
        pass

    def get_user(self, user_name):
        accounts = self.environment.database.get_accounts()
        for account in accounts:
            if account["name"] == user_name:
                return User.User(account["name"], account["role"])
        return None

    def course_exists(self, course_number):
        courses = self.environment.database.get_courses()
        for course in courses:
            if course["number"] == course_number:
                return True
        return False

    def course_assigned(self, course_number):
        course_assignments = self.environment.database.get_course_assignments()
        for assignment in course_assignments:
            if assignment["course_number"] == course_number:
                return True
        return False

    def is_valid_role(self, role):
        roles = ["supervisor", "administrator", "instructor", "TA"]
        return role in roles
