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
        print("Помилка ділення на 0 неможливе!")
        return None


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: будь ласка, водьте числа.")



def calculator():
   print("Калькулятор \nДля завершення роботи введіть 'exit' ")
   
   while True:
        try:
            oper = input("Виберіть операцію (+, -, /, *): ").strip()

            if oper.lower() == 'exit':
                print("Программа завершена")
                break

            if oper not in ['+', '-', '*', '/']:
                raise ValueError("Невідома операція!")

            a = get_number("Введіть перше число: ")
            b = get_number("Введіть друге число: ")

            if oper == '+':
                result = add(a, b)
            elif oper == '-':
                result = subt(a, b)
            elif oper == '*':
                result = multi(a, b)
            elif oper == '/':
                result = div(a, b)

            if result is not None:
                print(f"Результат: {result}\n")

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Невідома помилка: {e}")
            
            if name == "__main__": calculator()


if __name__ == "__main__":
    calculator()