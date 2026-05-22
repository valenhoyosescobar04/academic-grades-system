import pytest
from src.academic_grades import GradeSystem

def test_register_valid_grade():
    system = GradeSystem()
    system.register_grade("Laura", "Calculus", "2025-1", 3.8)

def test_reject_negative_grade():
    system = GradeSystem()
    with pytest.raises(ValueError):
        system.register_grade("Laura", "Calculus", "2025-1", -1.0)

def test_reject_grade_above_maximum():
    system = GradeSystem()
    with pytest.raises(ValueError):
        system.register_grade("Laura", "Calculus", "2025-1", 6.5)

def test_accept_minimum_boundary():
    system = GradeSystem()
    system.register_grade("Laura", "Calculus", "2025-1", 0.0)

def test_accept_maximum_boundary():
    system = GradeSystem()
    system.register_grade("Laura", "Calculus", "2025-1", 5.0)

def test_reject_just_above_maximum():
    system = GradeSystem()
    with pytest.raises(ValueError):
        system.register_grade("Laura", "Calculus", "2025-1", 5.1)

def test_pass_with_exact_minimum():
    system = GradeSystem()
    system.register_grade("Laura", "Calculus", "2025-1", 3.0)
    assert system.passed("Laura", "Calculus") is True

def test_fail_just_below_threshold():
    system = GradeSystem()
    system.register_grade("Laura", "Physics", "2025-1", 2.9)
    assert system.passed("Laura", "Physics") is False

def test_fail_with_minimum_grade():
    system = GradeSystem()
    system.register_grade("Laura", "History", "2025-1", 0.0)
    assert system.passed("Laura", "History") is False

def test_average_with_multiple_grades():
    system = GradeSystem()
    system.register_grade("Laura", "Calculus", "2025-1", 2.0)
    system.register_grade("Laura", "Physics", "2025-1", 4.0)
    system.register_grade("Laura", "History", "2025-1", 3.0)
    assert system.average("Laura") == 3.0

def test_average_with_single_grade():
    system = GradeSystem()
    system.register_grade("Laura", "Calculus", "2025-1", 4.5)
    assert system.average("Laura") == 4.5

def test_average_with_no_grades():
    system = GradeSystem()
    assert system.average("Laura") == 0.0