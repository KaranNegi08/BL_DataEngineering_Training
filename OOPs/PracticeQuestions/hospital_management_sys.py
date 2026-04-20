from abc import ABC, abstractmethod
import datetime

class Person(ABC):
    def __init__(self,name, age):
        self.name=name
        self.age = age

    @abstractmethod
    def get_details(self):
        pass
        
# PATIENT CLASS
class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id= patient_id
        self.medical_history= []

    def add_history(self,record):
        self.medical_history.append(record)

    def get_details(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}"


# DOCTOR CLASS
class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization= specialization

    def get_details(self):
        print(f"Dr. {self.name} ({self.specialization})")



class Appointment:
    def __init__(self,patient,doctor, date):
        self.patient=patient
        self.doctor= doctor
        self.date= date

    def show_appointment(self):
        return f"{self.date} - {self.patient.name} with {self.doctor.name} "


class Billing:
    pass


class HospitalSystem:
    pass


def main():
    system= HospitalSystem()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. Show Appointments")
        print("5. Generate Bill")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient name: ")
            age= int(input("Enter patient age: "))
            patient_id = int(input("Enter patient id: "))

            system.add_patient((Patient(name,age,patient_id)))


