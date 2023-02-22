MENU = "l) Login, q) Quit"
# MENU is in caps because it's a CONSTANT
# The CONSTANT is a variable that never changes its value
# A variable is a box to put things in
# Function must always have a bracket

print(MENU)
valid_username = "Alexander"
valid_password = "password"
valid_birthday = "1984"

user_choice = input("Choose [l/q]: ")

if user_choice == "l":
    print("logging you in...")
    entered_username = input("Enter you're username: ")
    entered_password = input("Enter you're password: ")
    entered_birthday = input("Enter you're birthday: ")
    if entered_username == valid_username and entered_password == valid_password:
        print("You successfully logged in. ")
        if entered_birthday == valid_birthday:
            print("correct")
        else:
            print("wrong BD")
        # "and" instead of "or because and is strict "and" you need it for both password and username "or" is tolerant

    else:
        print("Invalid credentials")

elif user_choice == "q":
    print("quitting the program...")
else:
    print("Invalid choice")
