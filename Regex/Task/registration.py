import re
import os
import json

def load_users():
    try:
        if not os.path.exists("student_data.json"):
            with open("student_data.json", "w") as f:
                json.dump([],f)
            return []

        with open("student_data.json", "r") as f:
            return json.load(f)
        
    except Exception as e:
        print("Error occured while loading user..", e)
        return []



def save_users(users):
    try: 
        with open("student_data.json","w") as f:
            json.dump(users,f, indent=4)
    except Exception as e: 
        print("Error while saving data..", e)


def validate_name(name):
    return bool(re.match(r"^[A-Za-z ]{3,}$", name))


def validate_email(email):
    return bool(re.match(r"^[a-zA-Z0-9]+@gmail\.com$", email))


def validate_password(password):
    pattern = r"^[a-zA-Z0-9]{8,}$"
    return bool(re.match(pattern, password))

def create_account():
    try:
        name = input("Enter Name: ")
        if not validate_name(name):
            raise ValueError("Invalid Name!")

        email = input("Enter Email: ")
        if not validate_email(email):
            raise ValueError("Invalid Email!")


        password = input("Enter Password: ")
        if not validate_password(password):
            raise ValueError("Weak Password!")

        users = load_users()

        for user in users:
            if user["email"] == email:
                raise ValueError("Email already exists!")

        users.append({
            "name": name,
            "email": email,
            "password": password
        })

        save_users(users)
        print("Account Created Successfully!")

    except ValueError as ve:
        print("Invalid credentials...", ve)
    except Exception as e:
        print("Unexpected Error:", e)



def check_credentials(email, password):
    try:
        users = load_users()
        for user in users:
            if user["email"] == email and user["password"] == password:
                return True
        return False
    except Exception as e:
        print("Error:", e)
        return False


def login():
    try:
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if check_credentials(email, password):
            print("Login Successful!")
        else:
            print("Invalid Email or Password")

    except Exception as e:
        print("Login Error:", e)

def main():
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


main()