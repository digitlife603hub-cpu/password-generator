🚀 Password Generator v2.0 Update
✨ New Features
Refactored the program into functions for better organization.
Added input validation using try and except to prevent crashes from invalid input.
Implemented a while True loop to repeatedly prompt the user until a valid password length is entered.
Replaced the random module with Python's secrets module for cryptographically secure password generation.
Used secrets.SystemRandom().shuffle() to securely shuffle the generated password.
Improved variable names for better readability and maintainability.
Added a welcome banner to give the program a cleaner interface.
Added a confirmation message before displaying the generated password.
Added a farewell message when the user chooses not to generate a password.
Removed unnecessary imports and cleaned up the overall code structure.
🛠️ Improvements
Better code organization through modular design.
Improved readability with meaningful function and variable names.
Enhanced security by using a module designed for password generation.
Better user experience with clearer prompts and messages.
More maintainable and scalable code for future updates.
📚 Concepts Learned
Functions (def)
Returning values with return
Error handling (try / except)
Infinite loops with while True
Input validation
The secrets module
Secure randomization
String manipulation
Lists and shuffling
F-strings
Clean code practices
📌 Version History
Version 1.0
Generated random passwords.
Allowed the user to choose a minimum password length (8+).
Included uppercase, lowercase, numbers, and special characters.
Used the random module.
Version 2.0
Refactored into functions.
Added robust error handling.
Switched to the secrets module for secure password generation.
Improved user interface.
Improved code readability and maintainability.
Added secure password shuffling.