Restaurant Order Management System
Overview
The Restaurant Order Management System is a Python-based application designed to streamline the food ordering process. It provides an interactive interface for customers or staff to view the menu, select items, and generate a final bill automatically.
This project aims to simplify billing calculations and order tracking for small to medium-sized eateries.
Repository Structure
Plaintext
├── rest.py          # Entry point for the ordering system
├── menu.py          # Module handling menu items and prices
├── order.py       #  Module for calculating totals and tax
└── README.md        # Project documentation


Features
Interactive Menu: Displays a list of available food items with prices.
Order Taking: Allows users to select multiple items by ID or Name.
Bill Calculation: Automatically sums up the total cost.
Error Handling: Validates user inputs (e.g., prevents ordering invalid item numbers).
User-Friendly Interface: Simple Command Line Interface (CLI) for quick usage.
Prerequisites
Python 3.x installed on your system.

Installation
Clone the repository:
		Bash
		git clone https://github.com/ravirai0207-ctrl/Restraunt_Order.git
Navigate to the directory:
Bash
cd Restraunt_Order
Run the application:
	Bash
	python main.py

 Usage Example

Welcome to The Python Restaurant!
---------------------------------
1. View Menu
2. Place Order
3. Exit
: 1

--- Menu ---
1. Pizza - $10
2. Burger - $5
3. Pasta - $8

Enter your choice: 2
Select Item Number: 1
Quantity: 2
Added 2 Pizzas to cart.

Total Bill: $20

Contributing
Fork the repository.
Create a feature branch (git checkout -b feature/NewMenu).
Commit your changes.
Push to the branch.
Open a Pull Request.
 License
This project is created by Raviprakash Rai.


