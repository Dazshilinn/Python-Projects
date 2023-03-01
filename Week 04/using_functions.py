def my_calculator():
    print(5 * 5)


my_calculator()


def ask_for_name_and_greet():
    name = input("Enter your name: ")
    print("Welcome", name)


ask_for_name_and_greet()

is_adult = False


def verify_age_auto(the_age):
    if the_age >= 18:
        print("You may enter the club")
    else:
        print("Sorry we cannot let you in!")


# verify_age()


verify_age_auto(18)


def welcome(someone):
    print("Welcome", someone, "we're excited to see you here.")


welcome("Alexander")


def is_adult(an_age):
    if an_age >= 18:
        return True
    else:
        return False


if is_adult(50):
    print("Welcome")
else:
    print("Sorry")


def multiply_by_five(number):
    return 5 * number


print(multiply_by_five(5))
