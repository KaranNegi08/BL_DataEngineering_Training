from sqlalchemy.orm import Session

from models import Patient
from schema import PatientCreate
from db import get_db, Base


def create_patient(
    db: Session ,
    patient: PatientCreate
):
    db_patient = Patient(
        patient_id=patient.patient_id,
        fname=patient.fname,
        lname=patient.lname,
        age=patient.age,
        gender=patient.gender,
        email=patient.email,
        phone=patient.phone,
        city=patient.city
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient


def get_all_patients(db: Session):
    return db.query(Patient).all()


def get_patient_by_id(
    db: Session ,
    patient_id: int
):
    return (
        db.query(Patient)
        .filter(
            Patient.patient_id == patient_id
        )
        .first()
    )