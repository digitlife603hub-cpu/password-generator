# 🔐 Password Generator (Version 2)

## 📌 Description

An improved version of the beginner-friendly Python password generator. Version 2 builds on the original project by improving the code structure, adding better user interaction, and making the password generation process more reliable.

The program creates strong random passwords based on user-selected preferences while including lowercase letters, uppercase letters, numbers, and special characters.

## ⚙️ Features

* Generates random passwords
* Allows the user to choose the password length
* Requires a minimum password length
* Includes:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Special characters
* Ensures different character types are included
* Improved input validation
* Better organized code compared to Version 1

## 🛠️ Technologies Used

* Python
* `random` module
* `string` module

## 🧠 Concepts Practiced

* Functions
* User input handling
* Conditional statements (`if` statements)
* While loops
* Lists
* String manipulation
* Python modules
* `.join()` method
* Random selection
* Code organization

## 🚀 How I Built This Project

1. Improved the structure of the Version 1 password generator.
2. Organized password generation steps into separate sections.
3. Used the `string` module to access different character groups:

   * Lowercase letters
   * Uppercase letters
   * Numbers
   * Symbols
4. Generated characters based on user requirements.
5. Shuffled the characters to create a random password.
6. Converted the list of characters into a final password using `.join()`.

## ▶️ How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Run the file:

```bash
python password_generator.py
```

## 📷 Example Output

Add a screenshot here showing the program running.

Example:

```
Do you want a password randomly generated? yes

How many characters do you want your password to be?
16

Generated Password:
gT8@pL2!xQ7#mR5$
```
