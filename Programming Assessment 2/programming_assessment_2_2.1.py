import time
import random
import string


# the accounts from the accounts.txt file that I need to verify the users
def read_file_into_dictionary():
    accounts_dictionary = {}  # this is initiating a blank dictionary
    accounts_file_in = open("accounts.txt", "r")
    for line in accounts_file_in:
        username, password = line.split(" ")  # splitting the value and key is what line.split does
        accounts_dictionary[username] = password.rstrip()  # adding each username and password into the dictionary
    accounts_file_in.close()
    return accounts_dictionary  # this is an output of a function


def view_accounts():
    accounts_file_in = open("accounts.txt", "r")
    for line in accounts_file_in:
        # https://www.pythonpool.com/wp-content/uploads/2020/02/Trimming-White-Space-in-Python.png
        username, password = line.strip().split(" ")
        # print("Username:", username, "Password:", password)
        print(f"{username:15s} {password}")
    accounts_file_in.close()


accounts = read_file_into_dictionary()
# menu for users to login
MENU = "l) Login, q) Quit, r) Register, v) View accounts"

print(MENU)

user_choice = input("Choose [l/q/r/v]: ")

if user_choice == "l":
    entered_username = input("Enter you're username:")
    entered_password = input("Enter you're password:")
    # the accounts_dictionary up till the entered_username is a value that I have given the key
    if entered_username in accounts and accounts[entered_username] == entered_password:
        print("Logging you in. ")

    else:
        print("incorrect username or password")

elif user_choice == "q":
    print("quitting the login and registering procedure")
    time.sleep(2)
    print("end of program")

elif user_choice == "r":
    new_user = input("Register new username:")
    new_pass = ""
    print("Would you like to enter a new password (1) or have one generated for you (2)?")
    password_option = input("1 or 2?: ")
    if password_option == "1":
        new_pass= input("Enter your custom password: ")
    elif password_option == "2":
        print("We'll generate a password for you...")
        include_digits = input("Would you like digits in your password? [y/n]: ").lower()
        include_symbols = input("would you like symbols in your password? [y/n]:").lower()

        #random_digit = random.choice(digits)  # Pick a random digit from digits
        #random_symbols = random.choice(symbols)  # Pick a random symbol from symbols
        #random_letter = random.choice(letters)  # Pick a random letter from letters
        #random_characters_combo = random.choice(characters_combo)
        # random module for this
    else:
        print("Invalid choice.")

    # open accounts.txt file to write and append at the end


elif user_choice == "v":
    view_accounts()

else:
    print("Invalid choice")
    # def login(username, password):
    """A function to check if the provided username and password are valid."""
