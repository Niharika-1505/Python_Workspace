c = 20
d = 10


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
