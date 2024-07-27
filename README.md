# Daily-Expenses-Sharing-Application
Overview
This is the backend implementation of a daily expenses sharing application. The application allows users to add expenses and split them using three different methods: equal amounts, exact amounts, and percentages. It manages user details, validates inputs, and generates downloadable balance sheets.

Features
User Management: Create and retrieve user details.
Expense Management: Add and manage expenses with different split methods.
Balance Sheet: View and download balance sheets showing individual and overall expenses.
Technical Requirements
User Management
Attributes: Each user should have an email, name, and mobile number.
Operations:
Create user.
Retrieve user details.
Expense Management
Operations:

Add expense.
Retrieve individual user expenses.
Retrieve overall expenses.
Download balance sheet.
Split Methods:

Equal: Split equally among all participants.
Exact: Specify the exact amount each participant owes.
Percentage: Specify the percentage each participant owes. (Ensure percentages add up to 100%).
Expense Calculation Examples
Equal:

Scenario: You go out with 3 friends. The total bill is 3000. Each friend owes 1000.
Exact:

Scenario: You go shopping with 2 friends and pay 4299. Friend 1 owes 799, Friend 2 owes 2000, and you owe 1500.
Percentage:

Scenario: You go to a party with 2 friends and one of your cousins. You owe 50%, Friend 1 owes 25%, and Friend 2 owes 25%.
Balance Sheet
Display:
Individual expenses.
Overall expenses for all users.
Download: Provide a feature to download the balance sheet.
Data Validation
User Inputs: Ensure all user inputs are valid.
Percentage Splits: Ensure percentages in the percentage split method add up to 100%.
Documentation
Clear Code Comments: Ensure all functions and critical sections of the code are commented for clarity.
Setup and Installation
Clone the repository:

bash
Copy code
git clone https://github.com/ArpanLeedan/Daily-Expenses-Sharing-Application.git
Navigate to the project directory:

bash
Copy code
cd Daily-Expenses-Sharing-Application
Install dependencies:

bash
Copy code
npm install
Set up environment variables: Create a .env file and add necessary environment variables.

env
Copy code
DB_CONNECTION_STRING=your_database_connection_string
PORT=3000
Run the application:

bash
Copy code
npm start
