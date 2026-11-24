# Week 6 — pytest and Programming-Based Testing
A simple Python based Bank Account Management System as part of the Week 6 assignment on Object Oriented Programming (OOP) and automated testing with pytest.

## Project Overview

This project provides fundamental OOP concepts in Python through a bank account module. It also includes an automated test suite to verify account operations, input validation and exception handling.

## Features
- Create a bank account with an account number, holder name and initial balance.
- Deposit money into an account.
- Withdraw money from an account.
- Check the current account balance.
- Display account details.
- Validate account information and transaction amounts.
- Prevent duplicate account numbers.

## Techn and Tools

- **Python** – Module development
- **pytest** – Automated testing
- **pytest-html** – HTML test report generation

## Project Structure

```text
Week_6_OOP/
│
├── bank_account.py
├── test_bank_account.py
├── .gitignore
│
└── reports/
    └── test_report.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Week_6_OOP
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install pytest pytest-html
```

## Running the Application

Run the bank account application using:

```bash
python3 bank_account.py
```

## Running Automated Tests

Execute the pytest test suite:

```bash
pytest -v
```


## Generating an HTML Test Report


```bash
pytest -v --html=reports/test_report.html --self-contained-html
```

Open the generated report in your browser:

```bash
xdg-open reports/test_report.html
```

## Testing Coverage

The automated test suite covers:

- Positive test cases
- Negative test cases
- Boundary value testing
- Exception handling
- Account creation and validation
- Deposit and withdrawal operations
- Balance verification
- Duplicate account number validation
- Output verification

Parametrized tests and pytest fixtures are used to improve test organization and reduce repetitive code.

---
