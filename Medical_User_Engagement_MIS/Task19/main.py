from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import engine, Base, get_db
from crud import create_patient, get_all_patients, get_patient_by_id
from schema import PatientCreate, PatientResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post(
    "/patients",
    response_model=PatientResponse
)
def create_patients(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return create_patient(
        db=db,
        patient=patient
    )


@app.get(
    "/patients",
    response_model=list[PatientResponse]
)
def get_patients(
    db: Session = Depends(get_db)
):
    return get_all_patients(db)


@app.get(
    "/patients/{patient_id}",
    response_model=PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = get_patient_by_id(
        db,
        patient_id
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient
