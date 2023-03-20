import random
import string
import time

random_number = random.randint(1, 1000)
print("Random number:", random_number)

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
characters_combo = letters + digits + symbols

print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)
print("Characters Combo:", characters_combo)
