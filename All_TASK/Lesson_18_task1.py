import re

class MyClass:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            raise ValueError("Invalid email address")

    @classmethod
    def validate(cls, email):
        # Regular expression pattern for email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False

# Example usage
try:
    obj = MyClass("example@example.com")
    print("Email is valid:", obj.email)
except ValueError as e:
    print(e)

try:
    obj = MyClass("invalid_email")
    print("Email is valid:", obj.email)
except ValueError as e:
    print(e)
