import random
import string

# Function to generate a password
def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length < 4:
        print("Password length should be at least 4 for stronger security.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to check password strength
def check_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

# Function to save password to a file
def save_password_to_file(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to passwords.txt")

# Main program
def main():
    print("Welcome to the Advanced Password Generator!")
    try:
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        use_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        if password:
            print(f"\nGenerated Password: {password}")
            strength = check_strength(password)
            print(f"Password Strength: {strength}")

            save_option = input("Do you want to save this password to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                save_password_to_file(password)
    except ValueError:
        print("Invalid input! Please enter valid options.")

if __name__ == "__main__":
    main()