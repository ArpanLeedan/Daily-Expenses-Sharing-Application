# Daily Expenses Sharing Application

## Overview

This is the backend implementation of a daily expenses sharing application. The application allows users to add expenses and split them using three different methods: equal amounts, exact amounts, and percentages. It manages user details, validates inputs, and generates downloadable balance sheets.

## Features

- **User Management:** Create and retrieve user details.
- **Expense Management:** Add and manage expenses with different split methods.
- **Balance Sheet:** View and download balance sheets showing individual and overall expenses.

## Technical Requirements

### User Management

- **Attributes:** Each user should have an email, name, and mobile number.
- **Operations:** 
  - Create user.
  - Retrieve user details.

### Expense Management

- **Operations:**
  - Add expense.
  - Retrieve individual user expenses.
  - Retrieve overall expenses.
  - Download balance sheet.

- **Split Methods:**
  1. **Equal:** Split equally among all participants.
  2. **Exact:** Specify the exact amount each participant owes.
  3. **Percentage:** Specify the percentage each participant owes. (Ensure percentages add up to 100%).

### Expense Calculation Examples

1. **Equal:**
   - Scenario: You go out with 3 friends. The total bill is 3000. Each friend owes 1000.

2. **Exact:**
   - Scenario: You go shopping with 2 friends and pay 4299. Friend 1 owes 799, Friend 2 owes 2000, and you owe 1500.

3. **Percentage:**
   - Scenario: You go to a party with 2 friends and one of your cousins. You owe 50%, Friend 1 owes 25%, and Friend 2 owes 25%.

### Balance Sheet

- **Display:** 
  - Individual expenses.
  - Overall expenses for all users.
- **Download:** Provide a feature to download the balance sheet.

### Data Validation

- **User Inputs:** Ensure all user inputs are valid.
- **Percentage Splits:** Ensure percentages in the percentage split method add up to 100%.

## Documentation

- **Clear Code Comments:** Ensure all functions and critical sections of the code are commented for clarity.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArpanLeedan/Daily-Expenses-Sharing-Application.git
Navigate to the project directory:

bash
Copy code
cd Daily-Expenses-Sharing-Application
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up environment variables: Create a .env file and add necessary environment variables.

env
Copy code
FLASK_APP=app.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3  # or your preferred database URI
Run the application:

bash
Copy code
flask run
Requirements File
Create a requirements.txt file with the following content:

txt
Copy code
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
python-dotenv==0.19.0
