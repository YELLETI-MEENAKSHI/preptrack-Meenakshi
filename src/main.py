# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# Validate student name
while True:
    student_name = input("Enter student name: ")

    if student_name != "":
        break

    print("Student name cannot be empty.")

# Registration number
registration_number = input("Enter registration number: ")

# Graduation year
graduation_year = int(input("Enter graduation year: "))

# Validate attendance
while True:
    attendance = float(input("Enter attendance percentage: "))

    if attendance >= 0 and attendance <= 100:
        print("Attendance accepted.")
        break

    print("Invalid attendance. Enter a value between 0 and 100.")

# Project completion validation
while True:
    project_input = input(
        "Has the student completed the required project? Enter yes or no: "
    )

    if project_input == "yes":
        project_completed = True
        break

    elif project_input == "no":
        project_completed = False
        break

    else:
        print("Invalid input. Enter only yes or no.")

# Profile verification validation
while True:
    profile_input = input(
        "Is the student profile verified? Enter yes or no: "
    )

    if profile_input == "yes":
        profile_verified = True
        break

    elif profile_input == "no":
        profile_verified = False
        break

    else:
        print("Invalid input. Enter only yes or no.")