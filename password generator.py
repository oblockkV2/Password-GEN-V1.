import random
import string

def generate_password():
    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    symbols = string.punctuation
    
    # Create lists of characters
    password_chars = (
        random.sample(uppercase_letters, 5) +
        random.sample(lowercase_letters, 5) +
        random.sample(symbols, 5)
    )
    
    # Shuffle the characters to randomize their order
    random.shuffle(password_chars)
    
    # Join the list into a string and return
    return ''.join(password_chars)

def save_passwords_to_file(filename, num_passwords):
    with open(filename, 'w') as file:
        for _ in range(num_passwords):
            password = generate_password()
            file.write(password + '\n')

# Generate and save 100 passwords to 'passwords.txt'
save_passwords_to_file('passwords.txt', 100)