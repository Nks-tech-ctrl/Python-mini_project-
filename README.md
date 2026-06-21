# Python Mini Projects

This repository contains two beginner-friendly Python projects developed while learning Python programming.

## Projects

### 1. Guess the Number Game

A console-based game where the computer randomly selects a number, and the player must guess it within a limited number of attempts.

#### Features

* Easy, Medium, and Hard difficulty levels
* Different attempt limits for each difficulty
* Random number generation
* Input validation using `try-except`
* Attempt counter
* Quit option
* Displays the correct answer when attempts are exhausted

#### Difficulty Levels

| Difficulty | Range   | Attempts |
| ---------- | ------- | -------- |
| Easy       | 1 - 50  | 10       |
| Medium     | 1 - 100 | 7        |
| Hard       | 1 - 200 | 5        |

#### Concepts Used

* Variables
* Loops (`while`)
* Conditional Statements (`if-elif-else`)
* Exception Handling (`try-except`)
* Random Module
* User Input

#### Sample Output

```text
Select Difficulty Level!
1. Easy (1-50)
2. Medium (1-100)
3. Hard (1-200)

Enter choice (1/2/3): 2

Choose Number between 1 and 100!

Enter your Target number: 50
Your guess is small, guess again!

Enter your Target number: 75
Success: Correct Guess
Attempt: 2
```

---

### 2. Random Password Generator

A Python program that generates secure random passwords of user-defined length.

#### Features

* User chooses password length
* Minimum length validation
* Guaranteed uppercase letter
* Guaranteed lowercase letter
* Guaranteed digit
* Guaranteed special character
* Randomized password arrangement

#### Concepts Used

* Lists
* Loops
* String Manipulation
* Random Module
* String Module
* Input Validation

#### Sample Output

```text
Enter password Length : 12

Your random Password is :
A#7mP!2qX@9d
```

---

## Technologies Used

* Python 3

## How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-mini-projects.git
cd python-mini-projects
```

### Run Guess Number Game

```bash
python Guess_Number.py
```

### Run Password Generator

```bash
python Random_password_Generator.py
```

---

## Learning Outcomes

These projects helped practice:

* Python Basics
* Loops and Conditions
* Exception Handling
* String Handling
* Random Number Generation
* Input Validation
* Problem Solving

---

## Author

**Nikhil Singh**

