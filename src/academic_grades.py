class GradeSystem:
    def __init__(self):
        self.grades = []

    def register_grade(self, student, subject, semester, grade):
        if grade < 0.0 or grade > 5.0:
            raise ValueError("Grade must be between 0.0 and 5.0")
        self.grades.append({
            "student": student,
            "subject": subject,
            "semester": semester,
            "grade": grade
        })