# Sales Analytics System

## Overview
This project is a simple Sales Analytics System developed using Python.  
It reads sales data from a text file, cleans and validates the data, removes
invalid records, and calculates total sales revenue.

---

## Features
- Reads sales data from a text file
- Handles file encoding issues
- Removes header and empty lines
- Validates records based on business rules
- Cleans inconsistent product names
- Calculates total sales revenue

---

## Data Validation Rules
A record is removed if:
- Transaction ID does not start with "T"
- Quantity is less than or equal to zero
- Unit price is less than or equal to zero
- Customer ID is missing
- Region is missing

---

## Files Used
- `main.py` → Main Python program
- `sales_data.txt` → Input sales data file

---

## How to Run
1. Place `main.py` and `sales_data.txt` in the same folder  
2. Open terminal in that folder  
3. Run the command:

