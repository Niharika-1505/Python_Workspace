"""If condition"""
if (5 > 3):
    print("1. Hi")
"""If else condition"""
if 5 < 3:
    print("2. ", "Hello")
else:
    print("2. ", "Incorrect condition")
"""Elif condition"""
age = 16
if age < 16:
    print("3. Too young for alcohol")
elif age >= 16:
    print("3. Eligible for only certain alcohols")
else:
    print("3. You are old enough to consume any alcohol")

"""Operators"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("4. ", x is y)
print("5. ", x == y)
print("6. ", x is z)
print("7. ", "banana" in x)
print("8. ", "banana" not in x)
