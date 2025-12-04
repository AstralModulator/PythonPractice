# Encryption Program second attempt
import random
import string
def main():
    chars = " " + string.ascii_letters + string.punctuation + string.digits
    chars = list(chars)
    keys = chars.copy()
    random.shuffle(keys)

    secret_message = input("Enter the secret message: ")
    encrypted_message = ""
    for char in secret_message:
        index = chars.index(char)
        encrypted_message += keys[index]
    decrypted_message = ""
    for char in encrypted_message:
        index = keys.index(char)
        decrypted_message += chars[index]
    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)


if __name__ == '__main__':
    main()