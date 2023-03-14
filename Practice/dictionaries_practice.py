my_dictionary = {"author": "brandon sanderson", "book": "The Way of Kings"}

keys = my_dictionary.keys()
print(keys)

values = my_dictionary.values()
print(values)

items = my_dictionary.items()
print(items)

the_one = my_dictionary["book"]
print(the_one)

my_dictionary["novella"] = "dawnshard"

print(my_dictionary)

for my_key, my_value in my_dictionary.items():
    print(my_key, my_value, "-------")
print(my_dictionary["book"])