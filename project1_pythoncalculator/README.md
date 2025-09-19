# Calculator Projects (Summer 2025)

This repository contains two command-line calculator projects built with Python. Each version explores different approaches to parsing and evaluating arithmetic expressions. These projects are part of a larger summer learning goal and demonstrate your progress in mastering core programming concepts, algorithms, and safe evaluation practices.

---

## Project 1: Shunting Yard Algorithm Calculator

**File:** `calculator_shunting_yard.py`

### Features:

- Manual tokenization using regular expressions
- Implements the Shunting Yard algorithm to convert infix expressions to postfix
- Evaluates the postfix expression using a stack
- Handles:

  - Operator precedence and associativity
  - Negative numbers (with `-ve` input)
  - Decimals and scientific notation

### What I Learnt:

- Parsing user input
- Using regular expressions for tokenization
- Implementing classical algorithms (Shunting Yard)
- Stack-based expression evaluation
- Error handling (e.g., division by zero)

---

## Project 2: Safe Expression Evaluator (Asteval)

**File:** `calculator_asteval.py`

### Features:

- Accepts arithmetic expressions from the user
- Uses `asteval` for safe and secure evaluation
- Supports:

  - Negative numbers (`-ve` input)
  - Decimals and scientific notation

### What I Learnt:

- Secure evaluation of user input
- Replacing risky `eval()` calls with safer alternatives
- Regex token debug step (for learning)

---

## Requirements

- Python 3.8+
- [`asteval`](https://pypi.org/project/asteval/):

```bash
pip install asteval
```

---

## How to Run

```bash
python calculator_shunting_yard.py
# or
python calculator_asteval.py
```

---

## Learning Purpose

These projects were created to:

- Be the start of my python summer project journey
- Practice parsing logic and algorithms
- Understand the limitations of `eval()`
- Learn how real calculators handle precedence and expression evaluation

---

## Future Plans

- Add GUI version using Tkinter
- Extend to include variables and memory functions
- Integrate with a larger personal finance tracker project

---

## Author

**Kye Brathwaite**
Python Beginner – Summer 2025 Learning Journey

---

## Repository Structure

```
├── calculator_shunting_yard.py
├── calculator_asteval.py
└── README.md
```

---

Feel free to explore, and give feedback upon these foundational projects!
