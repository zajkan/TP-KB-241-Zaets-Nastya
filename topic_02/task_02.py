def sum(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    else:
        return a / b
print("Простий калькулятор")
print("Операції: +, -, /, *")
oper = input("Введіть операцію: ")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if oper == '+':
    print("Результат:", sum(a, b))
elif oper == '-':
    print("Результат:", subtract(a, b))
elif oper == '*':
    print("Результат:", multiply(a, b))
elif oper == '/':
    print("Результат:", divide(a, b))
else:
    print("Невідома операція!")