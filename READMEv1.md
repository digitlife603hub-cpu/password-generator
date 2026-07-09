# 🔐 Password Generator (Version 1)

## 📌 Description

A beginner-friendly Python password generator that creates random passwords based on user-selected length. The program automatically includes lowercase letters, uppercase letters, numbers, and special characters to generate stronger passwords.

## ⚙️ Features

* Generates random passwords
* Allows the user to choose the password length
* Requires a minimum password length of 8 characters
* Includes:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Special characters
* Shuffles generated characters to create a random password

## 🛠️ Technologies Used

* Python
* `random` module
* `string` module

## 🧠 Concepts Practiced

* User input
* Variables
* Conditional statements (`if` statements)
* While loops
* Lists
* String manipulation
* Python modules
* `.join()` method
* Random selection

## 🚀 How I Built This Project

1. Imported the `random` and `string` modules.
2. Used the string module to access different character groups:

   * Lowercase letters
   * Uppercase letters
   * Numbers
   * Symbols
3. Generated at least one character from each category.
4. Added extra random characters until the password reached the user's chosen length.
5. Used `random.shuffle()` to mix the characters.
6. Used `.join()` to convert the characters into a final password.

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
![alt text](image.png)
```
Do you want to a password randomly generated? yes

How many characters do you want your password to be?
12

Generated Password:
A7@kP2!mL9#q
```

## 🔮 Future Improvements (Version 2)

* Improve code structure using functions
* Add better error handling
* Replace `random` with `secrets` for stronger security randomness
* Add more customization options
