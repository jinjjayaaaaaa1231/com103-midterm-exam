# com103-midterm-exam
Weekly Expense Logger

Janine Athea P. Estallo | BSIT SE 1A

Project Overview

A Python console application designed to help students track their weekly spending. It allows for organized logging of expenses across five key categories, automatically flags high spending, and calculates the remaining balance.

Technical Features

Input Validation: Uses while loops to ensure category selection (0-5) is accurate.

High Expense Logic: Automatically tags any single purchase exceeding 25% of the total budget.

Dynamic Storage: Utilizes a nested list structure to store and retrieve expense details.

Budget Assessment: Provides a final status message based on whether the remaining balance is positive or negative.

Code Logic Flow
Initialization: Captures user name and total weekly budget.

The Entry Loop: Runs 4 times (expandable to 5), prompting for category, description, and cost.

Data Processing:

Converts category numbers to text names.

Calculates if the amount is a "High Expense."

Updates the total_spent running sum.

Final Report: Iterates through the stored list to print a formatted receipt and final budget status.
