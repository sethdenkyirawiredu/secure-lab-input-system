LAB INPUT SYSTEM
Overview
This project is a simple Python-based command-line program that demonstrates secure input handling and validation in a clinical laboratory context.
The system simulates how basic patient and laboratory data, such as patient name, age, sample ID, and haemoglobin value, can be collected safely while preventing invalid or unrealistic inputs from entering the workflow.
The focus of this project is secure coding habits, not advanced frameworks.
Features
•	Cleans user input using whitespace and case normalisation
•	Validates required text fields
•	Validates numeric input safely using error handling
•	Enforces realistic value ranges for laboratory results
•	Uses allow lists and format checks for sample IDs
•	Fails safely without crashing on invalid input

Why this project exists
In laboratory and healthcare systems, incorrect or poorly validated input can lead to:
•	Data integrity issues
•	Misinterpretation of results
•	Workflow interruptions
•	Patient safety risks
This project demonstrates how secure coding principles can be applied early, even in small scripts, to reduce these risks.

How it works
The program prompts the user to enter:
1.	Patient name
2.	Patient age
3.	Laboratory sample ID
4.	Haemoglobin value
Each input is validated before the program proceeds. If any value is invalid, the program stops and displays a clear message.
Only validated data is accepted for further processing.

Sample ID format
The sample ID must follow this format:
LAB-XXXX
Where XXXX represents numeric digits only.
Examples:
•	LAB-0001
•	LAB-2025
Acceptable value ranges
•	Patient age: 0 to 120 years
•	Haemoglobin: 5.0 to 25.0 g/dL
These ranges are used for demonstration purposes and can be adjusted.
How to run the program
1.	Make sure Python 3 is installed
2.	Clone the repository
3.	Navigate into the project directory
4.	Run the script:
python lab_input_system.py

Project structure
Secure Lab Input System/
├── src/
│   └── lab_input_system.py
├── README.md
├── .gitignore
└── requirements.txt


