def greet():
    print("Hello")

greet()

def get_name_and_greet():
    name = input("Enter you're name: ")
    print("Hello", name)

get_name_and_greet()

def verify_age():
    age = int(input("Enter you're age: "))
    if age >= 18:
        print("You're an adult")
    else:
        print("You're a minor")