import getpass
import hashlib

def get_password():
    """Prompts the user to enter a password"""
    password = getpass.getpass(prompt="Enter Password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash

def save_password():
    """Saves the password to a file"""
    password_hash = get_password()
    with open("passwords.key", "a") as f:
        f.write(f"{password_hash}\n")
    print("Password saved successfully.")

# Example usage
save_password()