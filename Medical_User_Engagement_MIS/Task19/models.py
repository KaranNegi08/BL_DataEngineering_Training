from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    age = Column(Integer)
    gender = Column(String(20))
    email = Column(String(100), unique=True)
    phone = Column(String(15))
    city = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())