def sum(a, b):
    return a + b
def subt(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    else:
        return a / b
print("Простий калькулятор")
print("Операції: +, -, /, *")
oper = input("Введіть операцію: ")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

match oper:
    case '+':
        print("Результат:", sum(a, b))
    case '-':
        print("Результат:", subt(a, b))
    case '/':
        print("Результат:", div(a, b))
    case '*':
        print("Результат:", multi(a, b))
    case _:
        print("Невідома операція!")