# Data Collections
# Lists
# Tuples
# Dict
# Lists

# syntax list_name=["addhh","asdfg","2erfghj"]

# Apply DRY
shopping_list =["ketchup","fanta","eggs","bread"]
# indexing    =    0           1     2      3
print(shopping_list)
print(type(shopping_list))
shopping_list.append("chicken")
#print()# add an item to the list
print(shopping_list)
shopping_list[2]="ice cream"
print(shopping_list)
# find out how to remove an item from the list
# find out how to remove fanta from the list
shopping_list.remove("fanta") # use remove method to delete an item from the list
print(shopping_list)
shopping_list.pop(1)
print(shopping_list)
multiple_type=[1 ,2,3,"one","two","three"]
print(multiple_type)
print(multiple_type[2])

# Tuple

# Immutable - cant be changed - edited- add

# user_details = DOB - country name - city name
# Syntax ("")

essentials = ("milk","paracetamol","drinks")
print(essentials)
print(type(essentials))
# what is the diff between Lists & Tuples
essentials[0]="coffee"