"""
Building a Caesar Cipher
"""

def encrypt(msg,key):
    res = ""
    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            res += chr(shifted)
        else:
            res += char
    return res

def decrypt(msg,key):
    return encrypt(msg,-key)

print('Secreat msg program')
choice = input('DO you want to E or D').strip().lower()

if choice == 'e':
    text = input('Enter your msg:\n')
    try:
        key = int(input('Enter a number between 1 and 25'))
        encryptd = encrypt(text,key=key)
        print('Encrepted msg\n')
        print(encryptd)

    except ValueError:
        print('Invalid KEY')
elif choice == 'd':
    text = input('Enter your msg:\n')
    try:
        key = int(input('Enter a number between 1 and 25'))
        decryptd = decrypt(text,key=key)
        print('Encrepted msg\n')
        print(decryptd)

    except ValueError:
        print('Invalid KEY')
else:
    print('Invalid Choice')