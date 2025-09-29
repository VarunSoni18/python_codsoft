import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    # Ask user for password length
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < 4:
                print("Password length should be at least 4 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
