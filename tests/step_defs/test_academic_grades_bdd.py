import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from src.academic_grades import GradeSystem

scenarios("../features/academic_grades.feature")

@pytest.fixture
def grade_system():
    return GradeSystem()

@given("a new grade system", target_fixture="grade_system")
def new_grade_system():
    return GradeSystem()

@when(parsers.parse("I register a grade of {grade:f} for \"{student}\" in \"{subject}\" for semester \"{semester}\""))
def register_grade(grade_system, grade, student, subject, semester):
    grade_system.register_grade(student, subject, semester, grade)

@then(parsers.parse("\"{student}\" should pass \"{subject}\""))
def student_passes(grade_system, student, subject):
    assert grade_system.passed(student, subject) == True

@then(parsers.parse("\"{student}\" should fail \"{subject}\""))
def student_fails(grade_system, student, subject):
    assert grade_system.passed(student, subject) == False

@then(parsers.parse("the average for \"{student}\" should be {expected:f}"))
def check_average(grade_system, student, expected):
    assert grade_system.average(student) == pytest.approx(expected)

@then(parsers.parse("registering a grade of {grade:f} for \"{student}\" in \"{subject}\" for semester \"{semester}\" should fail"))
def register_duplicate_fails(grade_system, grade, student, subject, semester):
    with pytest.raises(ValueError):
        grade_system.register_grade(student, subject, semester, grade)