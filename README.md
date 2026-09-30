## Hostel/Mess Complaint Management System

1. Project Title

Hostel/Mess Complaint Management System

2. Project Overview

The Hostel/Mess Complaint Management System is a simple Python-based project designed to manage complaints related to hostel and mess facilities.

Students can register complaints, view all submitted complaints, and check their complaint status using a unique complaint ID. The system also provides an option to update complaint status.

This project is developed using basic Python concepts such as functions, loops, conditional statements, lists, and dictionaries.

3. Features

- Register hostel and mess complaints.
- Enter student name and room number.
- Select complaint category (Hostel or Mess).
- Generate a unique complaint ID.
- View all registered complaints.
- Check complaint status using the complaint ID.
- Update complaint status.
- Track complaints as Pending, In Progress, or Resolved.
- Simple menu-driven interface.

4. Technologies and Tools Used

- Programming Language: Python
- Code Editor: Visual Studio Code
- Data Structures: Lists and Dictionaries
- Version Control: Git and GitHub

5. Project Modules

5.1 Register Complaint

Allows students to enter their details and register a new complaint.

5.2 View All Complaints

Displays all registered complaints along with their details and current status.

5.3 Check Complaint Status

Allows users to check the status of a complaint using its unique ID.

5.4 Update Complaint Status

Allows the status of a complaint to be changed to Pending, In Progress, or Resolved.

5.5 Main Menu

Provides options to access different features and exit the program.

6. Installation and Setup

Step 1: Install Python

Download and install Python on your computer.

Step 2: Create a Project Folder

Create a folder named:

"Hostel-Mess-Complaint-System"

Step 3: Create the Python File

Inside the folder, create a file named:

"hostel_mess_complaint.py"

Step 4: Add the Source Code

Copy the Python source code into the file and save it.

7. How to Run the Project

Open the project folder in Visual Studio Code.

Open the terminal and run:

python hostel_mess_complaint.py

If the command does not work, try:

python3 hostel_mess_complaint.py

The main menu will appear in the terminal.

8. How to Use the System

After running the program, the following menu appears:

1. Register Complaint
2. View All Complaints
3. Check Complaint Status
4. Update Complaint Status (Admin)
5. Exit

Register a Complaint

Select option 1 and enter the student's name, room number, category, and complaint description.

View Complaints

Select option 2 to display all registered complaints.

Check Complaint Status

Select option 3 and enter the complaint ID to check its current status.

Update Complaint Status

Select option 4, enter the complaint ID, and select the new status.

Exit

Select option 5 to close the program.

9. Testing Instructions

The following test cases can be used to check the program:

Test Case| Expected Result
Register a Hostel complaint| Complaint is registered successfully
Register a Mess complaint| Complaint is registered successfully
Enter an invalid category| An error message is displayed
View complaints| All registered complaints are displayed
Check a valid complaint ID| Complaint details and status are displayed
Check an invalid complaint ID| Complaint ID not found message appears
Update complaint status| Status is updated successfully
Enter an invalid menu option| Invalid choice message appears

10. Data Storage

The project uses a Python list to store complaint records.

Each complaint is stored as a dictionary containing:

- Complaint ID
- Student Name
- Room Number
- Category
- Complaint Description
- Complaint Status

Note: Complaint data is stored temporarily in memory. It is lost when the program is closed.

11. Future Enhancements

- Add permanent data storage using a database.
- Add an admin login system.
- Add complaint priority and submission date.
- Add a search and filter option.
- Develop a graphical user interface.
- Add notifications when complaint status changes.

12. Project Objective

The main objective of this project is to provide a simple and organized way to register, manage, and track hostel and mess complaints while applying fundamental Python programming concepts.

13. Author

Name: Kamlesh Dhaker

Project: Hostel/Mess Complaint Management System

Course: Python Programming
