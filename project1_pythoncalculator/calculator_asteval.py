"""
calculator_asteval.py

A command-line calculator that safely evaluates arithmetic expressions using the `asteval` library.
This version avoids the risks of Python's built-in `eval()` function by using a safe interpreter.
Supports decimals, negatives, and scientific notation.

Author: Kye Brathwaite
Date: 15th June 2025
"""

import re
from asteval import Interpreter

# Input Phase
expression = []

while True:
    user_input = input("Enter a number, operator, or -ve (type '=' to calculate): ").strip().lower()

    if user_input == "=":
        break
    elif user_input == "-ve":
        num = input("Enter a number to make it negative: ").strip()
        expression.append("-" + num)
    else:
        expression.append(user_input)

# Join into a single string
expression_input = " ".join(expression)

# Optional debug print of tokenized input
regex = re.findall(r'-?(?:\d+\.\d+|\.\d+|\d+)(?:e[+-]?\d+)?|[-+*/%()]', expression_input, re.IGNORECASE)
print("Tokenized expression (debug):", regex)

# Evaluate expression using asteval
aeval = Interpreter()

try:
    result = aeval(expression_input)
    if result is not None:
        print("The result of your calculation was:", round(result, 2))
    else:
        print("Could not evaluate expression.")
except Exception as e:
    print("Error evaluating expression:", e)
