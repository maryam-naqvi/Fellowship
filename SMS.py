# SMS.py

class Student:
    def __init__(self, name, age, student_id, courses=None):
        try:
            self.set_name(name)
            self.set_age(age)
            self.set_student_id(student_id)
            self.set_courses(courses if courses is not None else {})
        except Exception as e:
            print(f"Error initializing Student: {e}")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self._age = age

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, student_id):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID must be a non-empty string.")
        self._student_id = student_id

    def get_courses(self):
        return self._courses

    def set_courses(self, courses):
        if not isinstance(courses, dict):
            raise ValueError("Courses must be a dictionary with course names and grades.")
        self._courses = courses

    def calculate_gpa(self):
        try:
            if not self._courses:
                return 0
            total = sum(self._courses.values())
            return round(total / len(self._courses), 2)
        except Exception as e:
            print(f"Error calculating GPA: {e}")

    def __str__(self):
        return f"Student: {self._name}, ID: {self._student_id}, GPA: {self.calculate_gpa()}"


class GraduateStudent(Student):
    def __init__(self, name, age, student_id, courses, thesis_title):
        super().__init__(name, age, student_id, courses)
        self.thesis_title = thesis_title

    def __str__(self):
        return f"Graduate Student: {self._name}, ID: {self._student_id}, Thesis: {self.thesis_title}, GPA: {self.calculate_gpa()}"


# Demonstration
if __name__ == "__main__":
    try:
        s1 = Student("Maryam", 20, "CS123", {"Math": 3.5, "Python": 4.0})
        print(s1)
        grad_s = GraduateStudent("Ahmed", 24, "CS555", {"AI": 3.8, "ML": 3.9}, "AI-Powered Security Systems")
        print(grad_s)
    except Exception as e:
        print(f"Error in demonstration: {e}")

