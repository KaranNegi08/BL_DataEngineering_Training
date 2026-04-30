class PatientValidationError(Exception):
    pass


def validate_patient(age, heart_rate):
    
    if age < 0 or age >120:
        raise PatientValidationError("Age must be greater than 0 and less than 120!!")
    
    if heart_rate <20 or heart_rate >220:
        raise PatientValidationError("Heart rate should be between 20 and 120!!")

    return True


