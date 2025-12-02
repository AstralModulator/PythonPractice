import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
print(chars)

key = chars.copy()
random.shuffle(key)

print(key)

plain_text = input("Enter your secret message: ")
cyphered_text = ""

for text in plain_text:
    index = chars.index(text)
    cyphered_text += key[index]
print(cyphered_text)

cyphered_text = input("Enter your cyphered message: ")
plain_text = ""
for text in cyphered_text:
    index = key.index(text)
    plain_text += chars[index]
print(plain_text)