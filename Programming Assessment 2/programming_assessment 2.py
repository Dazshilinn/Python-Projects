#  Create or open a file for the purposing of appending new and exiting users
file_out = open("accounts.txt")
file_out.close()

file_out = open("accounts_append.txt", "a")
file_out.close()

# asking user to validate usernames on the accounts txt file, Yes these are variables
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

# trying to get the information from above to be verified by reading the accounts.txt file
accounts_dictionary = {}
accounts_file_in = open("accounts.txt", "r")
if username in accounts_dictionary:
    print(username, "is correct")
else:
    print("incorrect username")

#for line in phonebook_file_in:

# making sure username and password are correct
#valid_username =
#valid_password =

