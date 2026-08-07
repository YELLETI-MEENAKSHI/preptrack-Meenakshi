# PrepTrack – Placement Preparation Performance Analyzer
# PrepTrack - Meenakshi
This is my first project repository

📘 PrepTrack – Placement Preparation Performance Analyzer

📌 Project Overview
PrepTrack is a Python console application that analyzes a student's placement preparation performance based on attendance, project completion, profile verification, and daily coding practice scores.

The application validates user input, evaluates performance, identifies strengths and weaknesses, and determines whether the student is ready for placement activities such as mock interviews.

✨ Features
Collects student details

Student Name
Registration Number
Graduation Year
Attendance Percentage
Project Completion Status
Profile Verification Status
Validates all user inputs

Non-empty student name
Graduation year between 2025–2027
Attendance between 0–100%
Accepts only "yes" or "no" for Boolean inputs
Accepts only scores between 0–100 or -1 for absence
Processes seven days of coding practice

Classifies each practice score into:
Strong (75–100)
Satisfactory (60–74)
Needs Improvement (40–59)
Critical (0–39)
Calculates

Total Score
Average Score
Attempted Days
Absent Days
Passed Days
Failed Days
Identifies

Highest Practice Score
Lowest Practice Score
First Critical Score
Evaluates placement readiness using multiple eligibility conditions.

Displays a detailed performance report.

📊 Placement Readiness Criteria
A student is considered Placement Ready only if all the following conditions are satisfied:

Graduation year is between 2025 and 2027
Attendance is at least 75%
At least 6 practice sessions attempted
Average score is at least 70
No critical score (<40)
At least 4 passed practice days
Required project completed
Student profile verified

🛠 Technologies Used
Python 3
Console-based Application
Loops
Conditional Statements
Input Validation
Boolean Logic
Variables and Counters

📂 Project Structure
PrepTrack/
│
├── main.py
└── README.md

▶️ How to Run
Install Python 3.
Download or clone this repository.
Open a terminal in the project folder.
Run:
python main.py
Enter the required student details and practice scores.

📋 Sample Report
The application displays:

Student Information
Attendance
Practice Statistics
Performance Classification
Total and Average Scores
Highest and Lowest Scores
First Critical Score (if any)
Final Placement Status
Primary Blocker
Recommended Next Action

📖 Concepts Demonstrated
Input Validation
While Loops
For Loops
Conditional Statements
Boolean Variables
Counters
Nested Conditions
Data Classification
Performance Analysis
Report Generation

🎯 Learning Outcomes
By completing this project, learners will understand how to:

Validate user input
Process repeated data using loops
Apply conditional logic
Maintain counters and accumulators
Calculate totals and averages
Track minimum and maximum values
Generate structured reports
Build a complete console-based Python application

👨‍💻 Author
Developed as a Python programming project for practicing problem-solving, input validation, loops, conditional logic, and performance analysis.
