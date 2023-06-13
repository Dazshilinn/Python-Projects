# Alexander Dexter 7/06/23 Authentication Program
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
    entered_username = input("Enter your username:")
    entered_password = input("Enter your password:")
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
    # the new_pass is a variable that will gather data to be placed into it from the lower code
    print("Would you like to enter a new password (1) or have one generated for you (2)?")
    password_option = input("1 or 2?: ")
    if password_option == "1":
        new_pass = input("Enter your custom password: ")
    elif password_option == "2":
        print("We'll generate a password for you...")
        include_letters = input("Would you like the password to include letters? [y/n] ").lower()
        include_digits = input("Would you like digits in your password? [y/n]: ").lower()
        include_symbols = input("would you like symbols in your password? [y/n]: ").lower()
        password_length = input("Enter the length of the password (or press enter to use the default (10): ") or 10
        characters_combo = ""
        # characters_combo variable will now gather all the input data from the following user inputs
        if include_letters == "y":
            characters_combo += string.ascii_letters
        if include_digits == "y":
            characters_combo += string.digits
        if include_symbols == "y":
            characters_combo += string.punctuation

        # Repeat the action of picking a random character at a time to construct a password
        for character in range(int(password_length)):
            # pick a random choice of a character from the combination the user chose (letters/digits/symbols)
            a_character = random.choice(characters_combo)
            # add or append each newly picked character to the password to construct it
            new_pass += a_character

        print("Your Generated Password is: ", new_pass)

    else:
        print("Invalid choice.")
    file_out = open("accounts.txt", "a")
    file_out.write(f"{new_user} {new_pass}\n")
    file_out.close()


elif user_choice == "v":
    view_accounts()

else:
    print("Invalid choice")
