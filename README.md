# Calculator-in-Python
A graphical calculator built with Python and Tkinter library. This calculator can perform basic arithmetic operations, trigonometric functions, and handle mathematical constants like pi and e.

Features:
  Basic arithmetic operations: addition, subtraction, multiplication, and division
  Power function and exponential calculations
  Trigonometric functions: sin, cos, tan
  Logarithmic functions: log (base 10) and natural log (ln)
  Mathematical constants: pi and e
  Clear and evaluate functionalities

Requirements:
  Python 3.x
  Tkinter library (typically included with Python)

Installation:
  1. Clone the repository:
    git clone https://github.com/yourusername/Calculator.git
  2. Navigate to the project directory:
    cd Calculator
  3. Run the calculator:
    python calculator.py

Usage:
  Start the calculator by running calculator.py.
  Enter numbers and operations by clicking the corresponding buttons.
  Click = to evaluate the expression, or C to clear the display.

Code Overview
  This calculator is built using Python's Tkinter library for a graphical user interface. The    key components include:
    Display: A Tkinter Entry widget used to show the current input or result.
    Buttons: Tkinter Button widgets for numbers, operations, and functions. Each button has a      command that handles the associated action.
    Operations: A mix of standard arithmetic and scientific functions, using the math library      to handle trigonometry, logarithmic functions, and constants.
