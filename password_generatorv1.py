import random
import string


ques = input("Do you want to a password randomly generated? ")


p = ""
if ques.lower() == "no":
    print("Okay, have a nice day!")
    quit()

q = int(input("How many characters do you want your password to be atleast? It must be 8 characters or more, choose a number from 8 or more: "))
while q < 8:
    print("Please choose a number that is 8 or more.")
    q = int(input("How many characters do you want your password to be atleast? It must be 8 characters or more, choose a number from 8 or more: "))


if ques.lower() == "yes":
    
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    number = random.choice(string.digits)
    special = random.choice(string.punctuation)

    p += lower + upper + number + special
    s = list(p)
    random.shuffle(s)
    password = "".join(s)
    

    while len(password) < q:
        choices = [random.choice(string.ascii_lowercase), 
                   random.choice(string.ascii_uppercase), 
                   random.choice(string.digits), 
                   random.choice(string.punctuation)]
        password += random.choice(choices)




print(password)



