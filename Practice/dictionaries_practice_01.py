my_dictionary ={"author": "brandon sanderson", "book": "stormlight archive", "book number": "2" }

keys = my_dictionary.keys()
print(keys)

values = my_dictionary.values()
print(values)

items = my_dictionary.items()
print(items)

the_one = my_dictionary["book number"]
print(the_one)

my_dictionary["novella"] = "dawnshard"
print(my_dictionary)

for my_items in my_dictionary.items():
    print(my_items, "------")

print(my_dictionary["author"])