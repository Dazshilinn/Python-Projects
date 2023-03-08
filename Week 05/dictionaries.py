my_dictionary = {"firstname": "John", "lastname": "Smith", "postcode": 2000}

# Get the keys of a dictionary
keys = my_dictionary.keys()
print(keys)

# Get the values of a dictionary
values = my_dictionary.values()
print(values)

# get the items (pairs) of a dictionary
items = my_dictionary.items()
print(items)

# Get the value of a specific key in the dictionary
the_one = my_dictionary["lastname"]
print(the_one)

# Add a new item (pair) to the dictionary
my_dictionary["phone"] = "04040404"

print(my_dictionary)

# Use a for loop with .items() to neatly display keys and values of a dictionary
for my_key, my_value in my_dictionary.items():
    print(my_key, my_value, "-------")
print(my_dictionary["postcode"])
# variable = (3, 3, 3, 3,)
# print(type(keys))
