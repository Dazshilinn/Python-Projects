def Welcome():
    print("Welcome my son")

Welcome()

def get_name_and_Welcome():
    name = input("Enter you're name my son: ")
    print("Hello my son", name)

get_name_and_Welcome()

def get_age():
    age = int(input("please enter you're age: "))
    if age <= 18:
        print("you are too young my friend ")

    else:
        print("you are of the correct age to enter my son")

get_age()
