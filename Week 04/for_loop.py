cars = ["BMW", "Mercedes", "Ford"]

for car in cars:
    print("Car:", car)
# \n for the next printed string to go to the next line
for time in range(2):
    print("Hello\nHow are you?\nI'm fine")
# end will cause the print to go horizontal
for letter in range(10):
    print("x", end="")
# n, i and uppercase detector
word = input("\nEnter a word: ")
for letter in word:
    if letter == "n":
        print("The letter n was found in your word")
    if letter == "i":
        print("The letter i was found in your word")
    if letter == letter.upper():
        print("An upper case was detected")


