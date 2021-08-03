# Dictionaries
""" Assigning a Dictionary"""
Age = {"Niha": 26, "Chandu": 24, "Nikki": 24, "Kowshi": 25, "Kamal": 21, "Deepu": 16, "Teja": 16}
print("1.", Age)
"""Accessing a specific key value"""
print("2.", Age["Deepu"])
"""Appending the Dictionary"""
Age["Keerthi"] = 7
print("3.", Age)
"""Updating the key value"""
Age["Keerthi"] = 10
print("4.", Age)
"""Creating a new Dictionary"""
Age1 = {"Pranavi": 5, "Yatika": 3, "Hritvik": 3}
print("5.", Age1)
"""Deleting from a Dictionary"""
del Age1["Yatika"]
print("6.", Age1)
"""Length of a Dictionary"""
print("7.", len(Age))
"""Reason why Dictionaries should have Unique Keys"""
Value = {"a": 1, "a": 2, "a": 3}
print("8.", Value)

"""Combining two Dictionaries"""
Age.update(Age1)
print("9. Ages of my dear family members", Age)
