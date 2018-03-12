# Syed Hussain Ather
# Week 1 In-Class Assignment

# Create a list of dictionaries, with each dictionary denoting the attributes of a single person, as follows:

people = [
    {'name': 'Charlie', 'age': 35},
    {'name': 'Alice', 'age': 30},
    {'name': 'Eve', 'age': 20},
    {'name': 'Gail', 'age': 30},
    {'name': 'Dennis', 'age': 25},
    {'name': 'Bob', 'age': 35},
    {'name': 'Fred', 'age': 25}]

# Print the items in people as comma seperated values.

for dictionary in people:
    print(dictionary["name"] + "," + str(dictionary["age"]))

# Write a function that accepts the people list, and prints the items as comma separated values.

def print_items(list_of_dictionaries):
    for dictionary in list_of_dictionaries:
        print(dictionary["name"] + "," + str(dictionary["age"]))

# Sort people so that they are ordered by age, and print.
people = sorted(people, key=lambda x: x["age"])
people.sort(key=lambda x: x["age"])
print_items(people)
