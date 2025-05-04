# file_handling.py

def read_students(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Student Records:")
            for line in lines:
                print(line.strip())
            print(f"Total Students: {len(lines)}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def write_students(filename, students):
    try:
        with open(filename, 'w') as file:
            for student in students:
                file.write(f"{student}\n")
        print(f"Records written to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")


# Demonstration
if __name__ == "__main__":
    students = ["Maryam, 20, CS123", "Ahmed, 24, CS555"]
    write_students("student_output.txt", students)
    read_students("student_output.txt")
