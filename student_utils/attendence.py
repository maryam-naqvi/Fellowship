# student_utils/attendance.py

def attendance_percentage(total_classes, attended_classes):
    """Calculate attendance percentage."""
    try:
        if total_classes <= 0:
            raise ValueError("Total classes must be greater than zero.")
        return round((attended_classes / total_classes) * 100, 2)
    except Exception as e:
        print(f"Error calculating attendance: {e}")
