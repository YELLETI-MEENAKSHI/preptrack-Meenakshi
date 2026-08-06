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


# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

for day in range(1, 8):
    # Validate score
    while True:
        score = int(
            input(
                f"Enter Day {day} score from 0 to 100, or -1 for absent: "
            )
        )

        if score == -1 or (score >= 0 and score <= 100):
            break

        print("Invalid score. Enter -1 or a value between 0 and 100.")

    # Handle absent day
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result : Absent")
        continue

    # Attempted day
    attempted_days += 1
    total_score += score

    # Highest and Lowest score
    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # Classification
    if score >= 75:
        print(f"Day {day} Result : Strong")
        strong_days += 1

    elif score >= 60:
        print(f"Day {day} Result : Satisfactory")
        satisfactory_days += 1

    elif score >= 40:
        print(f"Day {day} Result : Needs Improvement")
        improvement_days += 1

    else:
        print(f"Day {day} Result : Critical")
        critical_days += 1

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

    # Passed / Failed
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

if attempted_days == 0:
    final_status = "No Practice Attempted"
    primary_blocker = "No practice sessions completed."
    next_action = "Attempt at least 6 practice sessions."

elif critical_score_found:
    final_status = "Critical Score Found"
    primary_blocker = "A practice score below 40 was found."
    next_action = "Improve weak topics and retake practice."

elif attempted_days < 6:
    final_status = "Insufficient Practice"
    primary_blocker = "Less than 6 practice sessions attempted."
    next_action = "Complete at least 6 practice sessions."

elif passed_days < 4:
    final_status = "Insufficient Passed Days"
    primary_blocker = "Less than 4 passed practice days."
    next_action = "Improve scores above 60."

elif average_score < 70:
    final_status = "Average Too Low"
    primary_blocker = "Average score is below 70."
    next_action = "Increase overall practice performance."

elif attendance < 75:
    final_status = "Attendance Too Low"
    primary_blocker = "Attendance below 75%."
    next_action = "Maintain attendance above 75%."

elif graduation_year < 2025 or graduation_year > 2027:
    final_status = "Graduation Not Eligible"
    primary_blocker = "Graduation year is outside the eligible range."
    next_action = "Check placement eligibility."

elif not project_completed:
    final_status = "Project Incomplete"
    primary_blocker = "Required project is not completed."
    next_action = "Complete the project."

elif not profile_verified:
    final_status = "Profile Not Verified"
    primary_blocker = "Profile verification is pending."
    next_action = "Verify the profile."

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to the mock interview."

if attempted_days > 0:
    print(f"Highest Score          : {highest_score}")
    print(f"Highest Score Day      : Day {highest_score_day}")
    print(f"Lowest Score           : {lowest_score}")
    print(f"Lowest Score Day       : Day {lowest_score_day}")
else:
    print("Highest Score          : Not Available")
    print("Highest Score Day      : Not Available")
    print("Lowest Score           : Not Available")
    print("Lowest Score Day       : Not Available")

print()

if critical_score_found:
    print(f"First Critical Day     : Day {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")
else:
    print("First Critical Day     : Not Applicable")
    print("First Critical Score   : Not Applicable")

print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")

print()
print("=" * 50)
print("PREPTRACK REPORT")
print("=" * 50)

print("Student Name :", student_name)
print("Registration Number :", registration_number)
print("Graduation Year :", graduation_year)
print("Attendance :", attendance)

print("Attempted Days :", attempted_days)
print("Absent Days :", absent_days)
print("Passed Days :", passed_days)
print("Failed Days :", failed_days)

print("Strong Days :", strong_days)
print("Satisfactory Days :", satisfactory_days)
print("Needs Improvement Days :", improvement_days)
print("Critical Days :", critical_days)

print("Total Score :", total_score)
print("Average Score :", round(average_score, 2))

print("Highest Score :", highest_score)
print("Highest Score Day :", highest_score_day)

print("Lowest Score :", lowest_score)
print("Lowest Score Day :", lowest_score_day)

print()

print("Final Status :", final_status)
print("Primary Blocker :", primary_blocker)
print("Next Action :", next_action)

print("=" * 50)