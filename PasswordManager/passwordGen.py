import string
# secrets is more secure than random
import secrets

def passwordGen(length=12, uppercase=True, lowercase=True, numbers=True, symbols=True):
    # Define the characters to be used in the password
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Generate random password
    password = ''.join(secrets.choice(characters) for i in range(length))

    return password


print(passwordGen(length=20))
