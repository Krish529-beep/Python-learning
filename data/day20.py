"""
Build a secure offline password valut
"""
import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def str_checker(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    is_digit = any(c.isdigit() for c in password)
    has_special = any(c in "<>!@#$%^&*()" for c in password)

    score = sum([length >= 8,has_special,has_upper,is_digit])
    return ['Weak','medium','strong','verystrong'][min(score,3)]

def add_credential():
    website = input('Website:').strip()
    username = input('username:').strip()
    password = input('password:').strip()

    strength = str_checker(password)

    line = f'{website} || {username} || {password}'
    encoded_line = encode(line)

    with open(VAULT_FILE,'a',encoding='utf-8') as f:
        f.write(encoded_line + '\n')

    print('Cread saved!!')

def view_cread():
    if not os.path.exists(VAULT_FILE):
        print('File not found')
        return

    with open(VAULT_FILE,'r',encoding='utf-8') as f:
        for line in f:
            data = decode(line.strip())
            website,username,password = data.split("||")
            hideen_password = '*' * len(password)
            print(f'{website} || {username} || {password} || {hideen_password}')

def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1": add_credential()
            case "2": view_cread()
            case "4": break
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()