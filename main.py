# main.py

from student_utils import arithmetic, attendance, performance

def main():
    # Arithmetic Utilities
    percentage = arithmetic.calculate_percentage(450, 500)
    print(f"Percentage: {percentage}%")
    grade = arithmetic.grade_classification(percentage)
    print(f"Grade: {grade}")

    # Attendance Utilities
    attend_perc = attendance.attendance_percentage(45, 40)
    print(f"Attendance: {attend_perc}%")

    # Performance Evaluation
    perf = performance.evaluate_performance(3.7)
    print(f"Performance: {perf}")

if __name__ == "__main__":
    main()
