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
print("Калькулятор \nДля завершення роботи введіть 'exit' ")
while True:
    oper = input("Введіть операцію (+, -, /, *) або 'exit': ")
    if oper.lower() == 'exit':
        print("Программа завершена")
        break
    try: 
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: будь ласка, водьте числа.")
        continue
    if oper == '+':
        print("Результат:", sum(a, b))
    elif oper == '-':
        print("Результат:", subt(a, b))
    elif oper == '*':
        print("Результат:", multi(a, b))
    elif oper == '/':
        print("Результат:", div(a, b))
    else:
        print("Невідома операція!")
