fruits = ["Apple", "Banana", "Cherry", "Durian"]
print("1.", fruits)
# Element at Position n
print("2.", fruits[0])
# sublist(from index, length of sublist)
print("3.", fruits[0:2])
# Appending a list
fruits.append("Elderberry")
print("4.", fruits)
# Updating a list nth position
fruits[3] = "Dates"
print("5.", fruits)
# Length of the list
print("6.", len(fruits))
fruitsListB = ["Fig", "Grapes", "Honeydew melon", "Ice Apple"]
# Concatenating lists
fruits = fruits + fruitsListB
print("7.", fruits)
# Deleting from list
del fruits[5]
print("8.", fruits)
# Deleting from index 2 until 5 but not 5
del fruits[2:5]
print("9.", fruits)

Ages = [10, 20, 30, 40]
# Maximum value in a list
print("10.", max(Ages))
# Minimum value in a list
print("11.", min(Ages))

# Repeating a list and concatenating it
fruits = fruits * 2
print("12.", fruits)
# Delete everything except last n in the list
del fruits[:-6]
print("13.", fruits)
# Deletes first n from the list
del fruits[:2]
print("14.", fruits)
fruits = fruits * 2
print("Appended List:", fruits)
# Deletes everything in the list from the index specified
del fruits[5:]
print("15.", fruits)
# Deletes last n elements
del fruits[-2:]
print("16.", fruits)
fruits = fruits * 3
