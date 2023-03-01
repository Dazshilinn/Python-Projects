user_choice = input("Enter l to login or q to quit")


def get_user_choice():
    print("Type l to login s to sign up q to quite")
    user_choice = input("Choose [l/s/q]: ").lower()
    if user_choice == "l":
        print("logging you in...")
    elif user_choice == "s":
        print("signing you up...")
    return user_choice


while get_user_choice() != "q":
    get_user_choice()
else:
    print("quitting the program...")

# Force someone to say yes
answer = input("yes or no: ")
while answer != "yes":
    answer = input("yes or no:")
