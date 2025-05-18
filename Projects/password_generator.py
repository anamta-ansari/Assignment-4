# password generator

import random
import string

num_passwords = int(input("How many passwords would you like to generate? "))
password_length = int(input("Enter the length of each password: "))

characters = string.ascii_letters + string.digits + string.punctuation

print("\nGenerated Passwords:")
for _ in range(num_passwords):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(password)
