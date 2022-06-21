from pyisemail import is_email


class Validator:

    @staticmethod
    def check_email(email):
        return is_email(email)

    @staticmethod
    def check_name(name):
        return len(name) > 2
