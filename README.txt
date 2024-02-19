# Employee Database Management System
----------------------------------------

This is a simple Employee Database Management System implemented in Python using MySQL as the backend database.

## Features
----------

- Add Employee to Database
- Display Employee Data
- Update Employee Data
- Promote Employee Data
- Remove Employee Data from Database
- Search Employee Data
- Exit

## Prerequisites
----------------

Before running the application, make sure you have the following:

- Python installed
- MySQL server running
- Required Python packages: `mysql.connector`

## Usage
-----------

1. Clone the repository or download the source code.

2. Open a terminal or command prompt.

3. Install the required Python packages:

```bash
pip install mysql-connector-python


1. Create a MySQL database and table:
------------------------------------

Run the script and provide your MySQL credentials (username and password).
Enter the desired database name when prompted.
The script will create the database and a table named empdata if they don't exist.
Run the main script:python main.py


Choose the desired operation from the menu and follow the instructions.

Custom Modules
--------------
This project uses the following custom modules:

1. add_employee.py: Contains functions to add employee data to the database.
2. display_employee.py: Contains functions to display employee data from the database.
3. update_employee.py: Contains functions to update employee data in the database.
4. promote_employee.py: Contains functions to promote employee data in the database.
5. remove_employee.py: Contains functions to remove employee data from the database.
6. search_employee.py: Contains functions to search for employee data in the database.



2. Employee Database Management System - Add Employee
----------------------------------------------------
This script is a part of the Employee Database Management System and is responsible for adding employee details into the database. The script prompts the user to input various employee details such as ID, Name, Email ID, Phone Number, Address, Post, and Salary. It validates the input data, checks if the employee ID and name already exist in the database, and then adds the employee to the database if all the information is valid.

Run the main script: python main.py

Choose the "Add Employee to Database" option from the menu.

Follow the instructions to enter the employee details:

- Employee Id: Enter a 5-digit unique numeric ID for the employee.
- Employee Name: Enter the employee's name.
- Employee Email Id: Enter a valid email address (e.g., example@gmail.com).
- Employee Phone Number: Enter a valid phone number (Indian format: 10 digits).
- Employee Address: Enter the employee's address.
- Employee Post: Enter the employee's job post or position.
- Employee Salary: Enter the employee's salary.
The script will validate the entered data and check if the ID and name are not already present in the database.

If the data is valid and the ID and name are unique, the script will add the employee to the database and display a success message.

Regular Expression Validation
-----------------------------

The script uses regular expressions to validate the following fields:

- Employee Id: It must be a 4-digit number (e.g., 1234).
- Employee Email Id: It must be a valid Gmail address (e.g., example@gmail.com).
- Employee Phone Number: It must be a valid Indian phone number (e.g., 9876543210).

Custom Modules
--------------
This script uses the following custom modules:

check_employee_id_exists.py: Contains a function to check if an employee ID already exists in the database.
employee_name_exists.py: Contains a function to check if an employee name already exists in the database.
main.py: Contains the main function for the Employee Database Management System.

Other custom modules (not shown here) are used for displaying employee data, updating employee data, promoting employees, removing employees, and searching for employees.




3. Employee Database Management System - Display Employee Details
--------------------------------------------------------------
This script is a part of the Employee Database Management System and is responsible for displaying employee details from the database. The script retrieves all employee data from the database and presents it in a user-friendly format.



Choose the "Display Employee Data" option from the menu.

The script will retrieve all employee data from the database and display it in the following format:



Employee Id: 1234
Employee Name: John Doe
Employee Email Id: johndoe@example.com
Employee Phone Number: 9876543210
Employee Address: 123 Main Street, City, Country
Employee Post: Manager
Employee Salary: 50000

Employee Id: 5678
Employee Name: Jane Smith
Employee Email Id: janesmith@example.com
Employee Phone Number: 9876543211
Employee Address: 456 Second Street, City, Country
Employee Post: Developer
Employee Salary: 40000
The data will be displayed for all employees in the database.

Custom Modules
--------------
This script uses the following custom module:

main.py: Contains the main function for the Employee Database Management System.


Other custom modules (not shown here) are used for adding employees, updating employee data, promoting employees, removing employees, and searching for employees.
Contributing

