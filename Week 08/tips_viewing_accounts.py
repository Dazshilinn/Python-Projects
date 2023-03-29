file_in = open("phonebook.txt", "r")

phonebook_dictionary = {}
for line in file_in:
    name, phone = line.split(" ")
    phonebook_dictionary[name] = phone.rstrip()
print(f"{'Name}':10s} Phone\n----------------------")
for name, phone in phonebook_dictionary.items():
    print(f"{name:10s} {phone}")

input()