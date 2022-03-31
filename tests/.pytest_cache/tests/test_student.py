import student
import pytest

def test_create_student():
    test_student1 = student.Student("Stu", "Dent",
                                    3.2, 119, 1001)
    assert test_student1.gpa == 3.2 and test_student1.credits ==119
    with pytest.raises(ValueError):
        student.Student("Cheat", "Ter", 9.7, 34, 1002)