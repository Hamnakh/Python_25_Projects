import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all characters
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Check if length is valid
    if length < 8:
        return "Password length must be at least 8 characters!"
    
    # Generate password
    password = []
    # Ensure at least one character from each set
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(digits))
    password.append(random.choice(special_chars))
    
    # Fill the rest of the password
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password characters
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

def main():
    while True:
        try:
            # Get desired password length from user
            print("\nPassword Generator")
            print("=================")
            length = int(input("Enter the length of your desired password (minimum 8): "))
            
            # Generate and display password
            password = generate_password(length)
            print("\nGenerated Password:", password)
            
            # Ask if user wants another password
            choice = input("\nDo you want to generate another password? (yes/no): ").lower()
            if choice != 'yes':
                print("Thank you for using the Password Generator!")
                break
                
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
