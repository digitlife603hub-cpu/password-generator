import secrets
import string

def get_password_length():
    while True:
        try:
            length = int(input("How many characters do you want your password to be at least? It must be 8 characters or more: "))
            if length < 8:
                print("Please choose a number that is 8 or more.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length):
    lower = secrets.choice(string.ascii_lowercase)
    upper = secrets.choice(string.ascii_uppercase)
    number = secrets.choice(string.digits)
    special = secrets.choice(string.punctuation)

    password = lower + upper + number + special
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = "".join(password_list)

    while len(password) < length:
        choices = [secrets.choice(string.ascii_lowercase), 
                   secrets.choice(string.ascii_uppercase), 
                   secrets.choice(string.digits), 
                   secrets.choice(string.punctuation)]
        password += secrets.choice(choices)

    final_password_list = list(password)
    secrets.SystemRandom().shuffle(final_password_list)
    final_password = "".join(final_password_list)

    return final_password

def main():
    user_choice = input("Do you want a password randomly generated? (yes/no): ").strip().lower()

    if user_choice == "no":
        print("\nOkay, have a nice day!\nThankyou for using the password generator!")
        return

    if user_choice == "yes":
        length = get_password_length()
        password = generate_password(length)
        print(f"\nYour generated password is: {password}")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("""=========================
 PASSWORD GENERATOR
=========================

Generate a secure password!""")
main()

