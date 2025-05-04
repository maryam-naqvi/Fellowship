# student_utils/arithmetic.py

def calculate_percentage(marks, total_marks):
    """Calculate percentage from marks."""
    try:
        if total_marks <= 0:
            raise ValueError("Total marks must be greater than zero.")
        return round((marks / total_marks) * 100, 2)
    except Exception as e:
        print(f"Error calculating percentage: {e}")


def grade_classification(percentage):
    """Classify grade based on percentage."""
    try:
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "Fail"
    except Exception as e:
        print(f"Error classifying grade: {e}")
