

---

🧮 Simple Calculator (Refactored)

A command-line calculator built with Python, featuring clean modular design, dynamic UI prompts, and a touch of personalized branding.

Originally written as a single script, this project has now been refactored into multiple well-documented modules for better maintainability, scalability, and readability.


---

 Features

Four basic arithmetic operations: Add, Subtract, Multiply, Divide

Dynamic UI system for handling user inputs and displaying menus

Last-result reuse — easily chain your previous results into new calculations

Graceful error handling, including invalid inputs and division by zero

Clean OOP design using separated logic and UI modules

Custom ASCII signature animation for branding and creative finish

Optional debug mode (powered by icecream) for development visibility



---

 Project Structure

simple_calculator/
│
├── operator_logic.py     # Handles arithmetic operations
├── calculator_ui.py      # Manages user interaction and menu flow
├── maker.py              # Generates and displays the custom signature
├── simple_calculator.py  # Main entry point (program controller)
└── README.md             # Project documentation


---

 How It Works

1. The main loop (in simple_calculator.py) handles user choices.


2. Each arithmetic operation is delegated to the OperatorLogic class.


3. All user interaction — menus, prompts, and result reuse — is handled by CalculatorUi.


4. The program ends with a custom animated signature from maker.py.




---

 Installation

Make sure you have Python 3.8+ installed.

Clone the repository and install dependencies:<b>

git clone https://github.com/Haashiraaa/simple-calculator-.git<br>
cd simple-calculator-<br>
pip install -r requirements.txt<b>

If you don’t have a requirements.txt, the only external dependency is:

pip install icecream emoji


---

▶ Usage

Run the program with:

python simple_calculator.py

You’ll be greeted with a Main Menu:

1. Add➕
2. Subtract➖
3. Multiply✖️
4. Divide➗
5. Quit🚫

Follow the on-screen instructions.
You can type = when done entering numbers to view your result.


---

 Example Session

Simple Calculator🔢

Main Menu
1. Add➕
2. Subtract➖
3. Multiply✖️
4. Divide➗
5. Quit🚫

Enter an option from 1 to 5
>>> 1

Enter numbers (enter '=' to see result)
number: 10
number: 5
number: =

 = 15


---

 Refactoring Summary

Converted from procedural to object-oriented architecture

Split logic into 3 clean modules:

OperatorLogic → arithmetic operations

CalculatorUi → UI interaction and input handling

Signature → animated branding art


Added PEP 8 compliance, docstrings, and inline comments

Integrated icecream debugging and graceful exception handling

Enhanced readability and modular extensibility



---

 Example Output

At program exit, the calculator displays a custom 3D ASCII signature:

/----------------/
             /|@@@@@@@@@@@@@@@/|
            / |##############/ |
           /  |#############/  |
          /   |############/   |
         /____|___________/    |
         |    |HAASHIRAAA |    |
         |    |___________|____|
         |   /Github:     |   /
         |  /@Haashiraaa  |  /
         | /X:            | /
         |/@Haashiraaa    |/
         -----------------


---


---

 License

This project is open-source and available under the MIT License.

