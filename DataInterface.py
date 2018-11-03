class DataInterface:
    def create_account(self, account_name, password, role):
        pass

    def delete_account(self, account_name):
        pass

    def update_account(self, account_name, password, role):
        pass

    def get_accounts(self):
        pass

    def get_logged_in(self):
        pass

    def set_logged_in(self, account_name):
        pass

    def set_logged_out(self):
        pass

    def create_course(self, course_number, course_name, ):
        pass

    def get_courses(self):
        pass

    def set_course_assignment(self, course_number, instructor_name):
        pass

    def get_course_assignments(self):
        pass

    def get_labs(self):
        pass

    def set_lab_assignment(self, course_number, lab_number, ta_name):
        pass

    def get_lab_assignments(self):
        pass
