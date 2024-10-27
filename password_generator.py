import random
import string

def generate_password(length, use_special_chars=True):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all characters
    all_characters = lower + upper + digits + special_chars
    
    # Ensure the password has at least one of each character type if complexity is high
    password = []
    if use_special_chars:
        password.append(random.choice(lower))
        password.append(random.choice(upper))
        password.append(random.choice(digits))
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password length
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the created password
    random.shuffle(password)
    
    return ''.join(password)

def main():
    # Get user input
    length = int(input("Enter the desired length of the password (at least 4): "))
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    if length < 4:
        print("Password length should be at least 4.")
        return
    
    # Generate and display the password
    password = generate_password(length, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
