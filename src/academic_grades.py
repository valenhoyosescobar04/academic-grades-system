MIN_GRADE = 0.0
MAX_GRADE = 5.0
PASSING_GRADE = 3.0

class GradeSystem:
    def __init__(self):
        self.grades = []

    def _validate_grade(self, grade):
        if grade < MIN_GRADE or grade > MAX_GRADE:
            raise ValueError(f"Grade must be between {MIN_GRADE} and {MAX_GRADE}")

    def register_grade(self, student, subject, semester, grade):
        self._validate_grade(grade)
        self.grades.append({
            "student": student,
            "subject": subject,
            "semester": semester,
            "grade": grade
        })

    def passed(self, student, subject):
        for record in self.grades:
            if record["student"] == student and record["subject"] == subject:
                return record["grade"] >= PASSING_GRADE
        return False
    
    def average(self, student):
        student_grades = [r["grade"] for r in self.grades if r["student"] == student]
        if not student_grades:
            return 0.0
        return sum(student_grades) / len(student_grades)