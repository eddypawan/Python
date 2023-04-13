import random
import string

def generate_password(length, uppercase, lowercase, numbers, special_characters):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Welcome to the Password Generator!\n")

password_length = int(input("Please enter the length of your password: "))
use_uppercase = input("Do you want to include uppercase letters? (y/n) ").lower() == 'y'
use_lowercase = input("Do you want to include lowercase letters? (y/n) ").lower() == 'y'
use_numbers = input("Do you want to include numbers? (y/n) ").lower() == 'y'
use_special_characters = input("Do you want to include special characters? (y/n) ").lower() == 'y'

generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_numbers, use_special_characters)
print("\nYour generated password is: " + generated_password)

while True:
    generate_another = input("\nDo you want to generate another password? (y/n) ").lower()
    if generate_another == 'y':
        generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_numbers, use_special_characters)
        print("\nYour generated password is: " + generated_password)
    elif generate_another == 'n':
        print("\nThank you for using the Password Generator!")
        break
    else:
        print("\nInvalid input. Please enter 'y' or 'n'.")
