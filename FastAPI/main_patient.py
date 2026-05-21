from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from crud import create_patient,get_all_patients,get_patient,delete_patient_db
from schemas import Patient, PatientUpdate

app= FastAPI()


@app.get('/')
def home():
    return {"message": "Patient Management API"}

@app.post("/create")
def create_patients(patient:Patient):
    existing = get_patient(patient.id)
    if existing:
        raise HTTPException(status_code=400, detail="Patient already exists")

    create_patient(patient)

    return JSONResponse(status_code=200, content={"message":"Patient created"})


@app.get("/view")
def view_patients():
    patients = get_all_patients()

    return patients

@app.get("/patient/{patient_id}")
def view_single_patient(patient_id: str):
    patient = get_patient(patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    patient = delete_patient_db(patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found") 

    return {"message":"Patient deleted"}