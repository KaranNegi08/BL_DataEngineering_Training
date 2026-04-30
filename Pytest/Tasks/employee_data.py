import re

def validate_id(emp_id):
    pattern = r'^EMP-\d{4}$'
    return re.match(pattern,emp_id, re.IGNORECASE)

def validate_email(email):
    pattern = r'^[a-zA-Z]\w+@company\.com$'
    return re.match(pattern,email, re.IGNORECASE)

def validate_employee(emp_id, email):

    if not validate_id(emp_id):
        raise ValueError("Invalid Emp Id...")

    if not validate_email(email):
        raise ValueError("Invalid Email...")

    return True


        

