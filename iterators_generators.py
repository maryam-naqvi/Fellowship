# iterators_generators.py

import random

class StudentList:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


def attendance_generator(students):
    """Yield attendance status randomly."""
    try:
        for student in students:
            yield (student, random.choice(["Present", "Absent"]))
    except Exception as e:
        print(f"Error in attendance generator: {e}")


def random_marks_generator(students, max_marks=100):
    """Yield random marks for each student."""
    try:
        for student in students:
            yield (student, random.randint(0, max_marks))
    except Exception as e:
        print(f"Error in marks generator: {e}")


# Demo
if __name__ == "__main__":
    students = ["Maryam", "Ahmed", "Ali"]
    student_list = StudentList(students)

    print("Iterating over students:")
    for s in student_list:
        print(s)

    print("\nAttendance:")
    for record in attendance_generator(students):
        print(record)

    print("\nRandom Marks:")
    for marks in random_marks_generator(students):
        print(marks)
