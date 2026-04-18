FILE_NAME = "student.txt"


def menu():
    while True:
        print("\nStudent Management System--")
        print("1. Add student")
        print(" 2. View student")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")
        

        choice= input("Enter the step: ")

        if choice =="1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting....")
            break
        else:
            print("Invalid command.")
            


def add_students():
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{marks}\n")

    print("Student record added successfully.")


def view_students():
    try:
        with open(FILE_NAME, "r") as f:
            data = f.readlines()

        if not data:
            print("record not found")
            return

        print("\nStudent records")
        for i in data:
            name, marks = i.strip().split(",")
            print(f"Name: {name} | Marks: {marks}")
        print()

    except FileNotFoundError:
        print("File not found.")


def search_student():
    name_to_search = input("Enter student name: ")
    found = False

    with open(FILE_NAME, "r") as f:
        for i in f:
            name, marks = i.strip().split(",")

            if name.lower() == name_to_search.lower():
                print(f"Name: {name} | Marks: {marks}")
                found = True
                break

    if not found:
        print("Student record not found!!!")


def update_student():
    name_to_update = input("Enter student name: ")
    marks_to_update = input("Enter new marks: ")

    updated = False
    lines = []

    with open(FILE_NAME, "r") as f:
        for i in f:
            name, marks = i.strip().split(",")

            if name.lower() == name_to_update.lower():
                lines.append(f"{name},{marks_to_update}\n")
                updated = True
            else:
                lines.append(i)

    with open(FILE_NAME, "w") as f:
        f.writelines(lines)

    if updated:
        print("Record updated successfully.")
    else:
        print("Student not found!!")


def delete_student():
    name_to_delete= input("Enter student name: ")
    deleted =False
    lines=[]
    with open(FILE_NAME, "r") as f:
        for i in f:
            name, marks= i.strip().split(",")

            if name.lower() != name_to_delete.lower():
                lines.append(i)
            else:
                deleted=True

    with open(FILE_NAME, "w") as f:
        f.writelines(lines)

    if deleted:
        print("Student record deleted.")
    else:
        print("Student not found.")

menu()