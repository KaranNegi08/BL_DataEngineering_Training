import pytest
from healthcare import validate_patient, PatientValidationError
def test_valid_patient():
    age=22
    heart_rate=120

    assert validate_patient(age, heart_rate) ==True


def test_invalid_age():
    age=130
    heart_rate=122
    
    with pytest.raises(PatientValidationError,match = "Age must be greater than 0 and less than 120!!"):
        validate_patient(age,heart_rate)


def test_invalid_heartrate():
    age=19
    heart_rate=12
    
    with pytest.raises(PatientValidationError,match = "Heart rate should be between 20 and 120!!"):
        validate_patient(age,heart_rate)