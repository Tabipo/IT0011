
while True:
    print("Student Record System")
    print("1. Open File")
    print("2. Save File")
    print("3. Save as File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\nOpening File...\n")
        file = open("student_record.txt", "r")
        print(file.read())
        file.close()

    elif choice == "2":
        print("\nSaving File...\n")
        exit()

    elif choice == "3":
        new_filename= input("Enter file name: ")
        print("Saving as File: " + new_filename)
        file = open("student_record.txt", "r")
        content = file.read()
        file = open(new_filename, "w")
        file.write(content)
        file.close()

    elif choice == "4":
        print("1. Order by Last Name")
        print("2. Order by Grade(60% Class Standing, 40% Major Exam)")
        Order_By = input("Enter your choice: ")
        if Order_By == "1":
            print("Showing All Students Record by Last Name")
            file = open("student_record.txt", "r")
            records = file.read().split("\n---------------------------------\n")
            file.close()

            records.sort(key=lambda record: record.split(" ")[1].split(": ")[1])
            for record in records:
                print(record)
            
        elif Order_By == "2":
            print("Showing All Students Record by Grade")
            file = open("student_record.txt", "r")

    elif choice == "5":
        find_student_id = input("Enter Student ID: ")
        file = open("student_record.txt", "r")
        records = file.read().split("\n---------------------------------\n")
        file.close()
        print("Searching Student Record: " + find_student_id)
        for record in records:
            if record.strip().startswith("Student ID: " + find_student_id):
                student_found = True
                print("Student Record Found:\n")
                print(record)


    elif choice == "6":
        file = open("student_record.txt", "a")
        student_id = input("Enter Student ID: ")
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        full_name = (fname, lname)
        course = input("Enter Course: ")
        class_standing = input("Enter Class Standing: ")
        major_exam = input("Enter Major Exam: ")

        print("Adding Record")
        students_record = (
            "\nStudent ID: {}\n"
            "Full Name: {}\n"
            "Course: {}\n"
            "Class Standing: {}\n"
            "Major Exam: {}\n"
            "---------------------------------\n"
        ).format(student_id, " ".join(full_name), course, class_standing, major_exam)
        file.write(students_record)
        file.close()
        print("Student Record Added\n")
    elif choice == "7":
        find_student_id = input("Enter Student ID: ")
        file = open("student_record.txt", "r")
        records = file.read().split("\n---------------------------------\n")
        file.close()

        updated_records = []
        student_found = False
        for record in records:
            if record.strip().startswith("Student ID: " + find_student_id):
                student_found = True
                print("Student Record Found:\n")
                print(record)
                print("\nEnter new data")
                student_id = input("Enter Student ID: ")
                fname = input("Enter First Name: ")
                lname = input("Enter Last Name: ")
                full_name = (fname, lname)
                course = input("Enter Course: ")
                class_standing = input("Enter Class Standing: ")
                major_exam = input("Enter Major Exam: ")
                new_record = (
                    "\nStudent ID: {}\n"
                    "Full Name: {}\n"
                    "Course: {}\n"
                    "Class Standing: {}\n"
                    "Major Exam: {}\n"
                ).format(student_id, " ".join(full_name), course, class_standing, major_exam)
                updated_records.append(new_record)
            else:
                updated_records.append(record)
        if student_found:
            file = open("student_record.txt", "w")
            file.writelines("\n---------------------------------\n" .join(updated_records))
            file.close()
            print("Student Record Updated\n")
        else:
            print("Student Record Not Found\n")
    elif choice == "8":
        find_student_id = input("Enter Student ID: ")
        file = open("student_record.txt", "r")
        records = file.read().split("\n---------------------------------\n")
        file.close()

        print("Searching for Student Record: " + find_student_id)

        updated_records = []
        student_found = False
        for record in records:
            if record.strip().startswith("Student ID: " + find_student_id):
                student_found = True
                print("Student Record Found:\n")
                print(record)
                print("\nDeleting Record...")
            else:
                updated_records.append(record)
        if student_found:
            file = open("student_record.txt", "w")
            file.writelines("\n---------------------------------\n" .join(updated_records))
            file.close()
            print("Student Record Updated\n")
        else:
            print("Student Record Not Found\n")