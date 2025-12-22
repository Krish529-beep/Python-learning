"""
Password Strength Checker and Suggestion
"""
import string
import random
import getpass

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short (min -8 char)")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit letter")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing special char")
    
    return issues
    

def generate_strong_passowrd(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation 
    
    return "".join(random.choice(chars)  for _ in range(length))


password = getpass.getpass("Enter a password:")
issues = check_password_strength(password)

if not issues:
    print("Strong password you are good to go")
else:
    print("You got weak password")
    for issue in issues:
        print(f'-{issue}')

print('\n suggesting you new strong password')
print(generate_strong_passowrd())
