from sqlalchemy import select
from db import SessionLocal
from models import Patients

def create_patient(patient):
    
    with SessionLocal() as session:
        db_patient= Patients(
            id=patient.id,
            name=patient.name,
            city=patient.city,
            age=patient.age,
            gender=patient.gender,
            height_cm=patient.height_cm,
            weight_kg=patient.weight_kg,
            bmi=patient.bmi,
            verdict=patient.verdict
        )
        
        session.add(db_patient)
        session.commit()

def get_all_patients():
    with SessionLocal() as session:
        stmt = select(Patients)
        patients = session.scalars(stmt).all()
        return patients

def get_patient(patient_id):
    with SessionLocal() as session:
        patient= session.get(Patients,patient_id)
        return patient

def delete_patient_db(patient_id):
    with SessionLocal() as session:
        patient= session.get(Patients, patient_id)

        if patient:
            session.delete(patient)
            session.commit()

        return patient