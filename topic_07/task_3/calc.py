from operations import Oper

def main():
	app = Oper()
	
	try:
		n1 = float(input("Введіть перше число: "))
		n2 = float(input("Введіть друге число: "))
		oper = input("Введіть дію (+ - * /): ")

		result = app.perform_operation(n1, n2, oper)
		print(f"Відповідь: {result}")
	except ValueError as e:
		print(f"Помилка: {e}")

if __name__ == "__main__":
	main()