Feature: Academic grade registration
  As a university administrator
  I want to register and manage student grades
  So that I can track academic performance by subject and semester

  Background:
    Given a new grade system

  @smoke
  Scenario: Student passes with minimum passing grade
    When I register a grade of 3.0 for "Laura" in "Calculus" for semester "2025-1"
    Then "Laura" should pass "Calculus"

  @smoke
  Scenario: Student fails with grade just below threshold
    When I register a grade of 2.9 for "Laura" in "Physics" for semester "2025-1"
    Then "Laura" should fail "Physics"

  @critical
  Scenario: Student fails with minimum possible grade
    When I register a grade of 0.0 for "Laura" in "History" for semester "2025-1"
    Then "Laura" should fail "History"

  @smoke
  Scenario: Average is calculated correctly with multiple grades
    When I register a grade of 2.0 for "Laura" in "Calculus" for semester "2025-1"
    And I register a grade of 4.0 for "Laura" in "Physics" for semester "2025-1"
    And I register a grade of 3.0 for "Laura" in "History" for semester "2025-1"
    Then the average for "Laura" should be 3.0

  @regression
  Scenario: Average for student with no grades returns zero
    Then the average for "Laura" should be 0.0

  @critical
  Scenario: System rejects duplicate grade for same subject and semester
    When I register a grade of 3.5 for "Laura" in "Biology" for semester "2025-1"
    Then registering a grade of 4.0 for "Laura" in "Biology" for semester "2025-1" should fail

  @regression
  Scenario: Same subject can be registered in a different semester
    When I register a grade of 3.5 for "Laura" in "Biology" for semester "2025-1"
    And I register a grade of 4.0 for "Laura" in "Biology" for semester "2025-2"
    Then the average for "Laura" should be 3.75

  @critical
  Scenario Outline: Students pass or fail based on their grade
    When I register a grade of <grade> for "Laura" in "Calculus" for semester "2025-1"
    Then "Laura" should <result> "Calculus"

    Examples:
      | grade | result |
      | 5.0   | pass   |
      | 3.0   | pass   |
      | 2.9   | fail   |
      | 0.0   | fail   |