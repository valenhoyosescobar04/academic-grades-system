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
        records = self._get_student_records(student)
        for record in records:
            if record["subject"] == subject:
                return record["grade"] >= PASSING_GRADE
        return False
    
    def average(self, student):
        records = self._get_student_records(student)
        if not records:
            return 0.0
        return sum(r["grade"] for r in records) / len(records)
    
    def _get_student_records(self, student):
        return [r for r in self.grades if r["student"] == student]