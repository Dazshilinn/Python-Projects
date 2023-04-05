phonebook_dictionary = {}

file_in = open("phonebook.txt")
for line in file_in:
    name, phone = line.split(" ")
    phonebook_dictionary[name] = phone.rstrip()

# Find if a name exists in the names
name = input("Enter a name to check if it exists: ")
if name in phonebook_dictionary.keys():
    print(name, "exists and his/her phone is", phonebook_dictionary[name])
else:
    print(f"No record of {name} is found")

# Validate a name and a phone number
entered_name = input("Enter a name: ")
entered_phone = input("Enter the phone number: ")
#if entered_name in phonebook_dictionary.keys(): and entered_phone == phonebook_dictionary[entered_name]:
 #   print("That is a valid record!")
#else:
  #  print("No such record exists.")