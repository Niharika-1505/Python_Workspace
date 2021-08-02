c = 10
d = 20


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def per(a, b):
    return a % b


funcs = [add, sub, mul, div, per]

for result in funcs:
    print(result(c, d))

firstName, lastName = "Niharika", "Gadde"
# Concatenating a String by adding
print("Author of this page is: " + firstName + " " + lastName)
# Repeating a String by multiplying
print("Hi " * 10)

sentence = "Niharika is typing this code"
# Printing character at a particular position - string[position]
print(sentence[0])
# Substring[Initial position of character : length of String]
print(sentence[0:8])
# Prints first n characters
print(sentence[:4])
# Prints complete String-n characters
print(sentence[:-3])

