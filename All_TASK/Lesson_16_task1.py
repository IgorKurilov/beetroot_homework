class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.classes = []

    def enroll(self, course):
        self.classes.append(course)
        print(f"{self.name} has enrolled in {course}.")

class Teacher(Person):
    def __init__(self, name, age, gender, subject, salary):
        super().__init__(name, age, gender)
        self.subject = subject
        self.salary = salary
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)
        print(f"{self.name} is now teaching {course}.")

    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary has been increased by {amount}. New salary: {self.salary}")

# Example usage:
student1 = Student("Alice", 16, "Female", "S123456")
student1.introduce()
student1.enroll("Mathematics")

teacher1 = Teacher("Mr. Smith", 35, "Male", "Mathematics", 50000)
teacher1.introduce()
teacher1.assign_course("Mathematics")
teacher1.increase_salary(5000)