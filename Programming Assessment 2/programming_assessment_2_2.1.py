import time
import random
import string

accounts_dictionary = {"fredsmart1": "12345678", "jrobertson4": "r@=%8(_W=1", "bob101": "1234598",
                       "marcusw": "3#tr@9dw%4}", "popeyedd": "1989eidjce", "junkman00": "p3*(kd8&ld",
                       "sbj2021": "$d5e(ep2(d", "robotman": "7777Spy007"}

MENU = "l) Login, q) Quit"

print(MENU)

user_choice = input("Choose [l/q]: ")

if user_choice == "l":
    entered_username = input("Enter you're username:")
    entered_password = input("Enter you're password:")
    # the accounts_dictionary up till the entered_username is a value that i have given the key
    if entered_username in accounts_dictionary and accounts_dictionary[entered_username] == entered_password:
        print("Logging you in. ")

    else:
        print("incorrect username or password")

elif user_choice == "q":
    print("quitting the login procedure")

    # def login(username, password):
    """A function to check if the provided username and password are valid."""
#   users = {
#      "alice": "password123",
#     "bob": "qwerty",
#    "charlie": "abc123"
# }

# if username in users and users[username] == password:
#    print("Login successful!")
# else:
# print("Invalid username or password.")

# Example usage
# login("alice", "password123")
# login("bob", "incorrectpassword")
