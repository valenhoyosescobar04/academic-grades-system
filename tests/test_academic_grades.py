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