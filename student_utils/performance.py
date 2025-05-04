# student_utils/performance.py

def evaluate_performance(gpa):
    """Evaluate performance based on GPA."""
    try:
        if gpa >= 3.5:
            return "Excellent"
        elif gpa >= 3.0:
            return "Good"
        elif gpa >= 2.0:
            return "Average"
        else:
            return "Poor"
    except Exception as e:
        print(f"Error evaluating performance: {e}")
.