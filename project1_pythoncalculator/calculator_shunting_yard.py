"""
calculator_shunting_yard.py

A command-line calculator built using the Shunting Yard algorithm for expression parsing
and postfix evaluation. This version manually handles operator precedence, associativity,
and supports negative numbers and scientific notation.

Author: Kye Brathwaite
Date: 15th June 2025
"""

import re

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '**': 3  # Exponentiation
}

associativity = {
    '+': 'left',
    '-': 'left',
    '*': 'left',
    '/': 'left',
    '%': 'left',
    '**': 'right'  # Exponentiation is right-associative
}

# Input phase
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

# Tokenization phase
expression_input = " ".join(expression)
regex = re.findall(r'\*\*|[-+*/%()]|-?(?:\d+\.\d+|\.\d+|\d+)(?:e[+-]?\d+)?', expression_input, re.IGNORECASE)

print("Your final expression was:", regex)

# Shunting Yard Algorithm 
def infix_to_postfix(tokens):
    """
    Converts infix expression to postfix using the Shunting Yard algorithm.
    """
    output = []
    stack = []

    for token in tokens:
        if re.match(r'-?(?:\d+\.\d+|\.\d+|\d+)(?:e[+-]?\d+)?', token):
            output.append(token)
        elif token in precedence:
            while stack and stack[-1] in precedence:
                top = stack[-1]
                if (associativity[token] == 'left' and precedence[token] <= precedence[top]) or \
                   (associativity[token] == 'right' and precedence[token] < precedence[top]):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('

    while stack:
        output.append(stack.pop())

    return output

# Convert to postfix
postfix = infix_to_postfix(regex)
print("Postfix expression:", postfix)

# Evaluate postfix expression
def evaluate_postfix(postfix_tokens):
    """
    Evaluates a postfix expression using a stack.
    """
    stack = []
    for token in postfix_tokens:
        if re.match(r'-?(?:\d+\.\d+|\.\d+|\d+)(?:e[+-]?\d+)?', token):
            stack.append(float(token))
            print("stack is:", stack)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '**':
                stack.append(a ** b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    print("Error: Division by zero.")
                    return None
                stack.append(a / b)
            elif token == '%':
                stack.append(a % b)

    return stack[0] if stack else None

# Final result
try:
    result = evaluate_postfix(postfix)
    if result is not None:
        print("The result of your calculation was:", round(result, 2))
except Exception as e:
    print("Error in expression:", e)
