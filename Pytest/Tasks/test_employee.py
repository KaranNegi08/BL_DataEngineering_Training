import pytest
from employee_data import validate_employee

def test_valid_employee():
    emp_id="EMP-0001"
    email="kunnu@google.com"

    assert validate_employee(emp_id, email) == True


def test_Invalid_id():
    emp_id="EMP-01"
    email="kunnu@google.com"

    with pytest.raises(ValueError, match= "Invalid Emp Id..."):
        validate_employee(emp_id, email) == True
    

def test_Invalid_email():
    emp_id="EMP-0001"
    email="1kunnu@google.com"

    with pytest.raises(ValueError, match= "Invalid Email..."):
        validate_employee(emp_id, email) ==True
