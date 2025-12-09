def add(a, b):
    return a + b

def subt(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка ділення на 0 неможливе!"