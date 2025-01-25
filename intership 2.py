import random
import string

# Generate a password
def generate_password(length):
    characters = string.ascii_letters + string.digits  # Letters and numbers only
    return ''.join(random.choice(characters) for _ in range(length))

# Main program
length = int(input("Enter password length: "))
password = generate_password(length)
print(f"Generated Password: {password}")
