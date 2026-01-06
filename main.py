students = {}

def add_student():
    name = input("Name: ")
    age = input("Age: ")
    students[name] = age
    print("Student added.")

def view_students():
    for name, age in students.items():
        print(f"{name} - {age}")

def main():
    while True:
        print("\n1.Add 2.View 3.Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()