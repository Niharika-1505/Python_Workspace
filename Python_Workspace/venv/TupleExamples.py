# Tuples

"""Creating a tuple"""
Value1 = (10, 20, 30)
Value2 = (40, 50, 60)
print("1.", Value1)
"""Accessing from tuple"""
print("2. ", Value1[0], ", ", Value2[0:2])
"""Concatenating tuples"""
Value1 += Value2
print("3.", Value1)
"""Deleting entire tuple"""
del Value2
"""Length of tuple"""
print("4.", len(Value1))
