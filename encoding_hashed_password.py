from cryptography.fernet import Fernet
import re


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()


def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message


def password_check(passwd):
    SpecialChar = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 8:
        print('length should be at 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialChar for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


def validate(password):
    if password_check(password):
        return True
    else:
        return False
