
from functions import add, subt, div, multi

def get_number():
	try:
		a = float(input("Введіть перше число: "))
		b = float(input("Введіть друге число: "))
		return a, b
	except ValueError:
		print("Помилка: введіть числове значення!\n")
		return None, None
	
def perform_operation():
   print("Калькулятор")
   while True:
        oper = input("Для завершення роботи введіть 'exit'\nВведіть операцію (+ - * /): ")
        if oper.lower() == "exit":
            print("Вихід з програми.")
            break
        if oper not in ['+', '-', '*', '/']:
             raise ValueError("Невідома операція!")
            
        a, b = get_number()
        if a is None or b is None:
            continue
      
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