import random

options = ["stone", "scissor", "paper"]

def game(user, bot):
	if user == bot:
		print("Нічия")
	elif (
		(user == "stone" and bot == "scissor") or
		(user == "paper" and bot == "stone") or
		(user == "scissor" and bot == "paper")):
		print("Ви перемогли!")
	else:
		print("Комп'ютер переміг")

def main():
	while True:
		user_choise = input("\nГра камінь, ножиці, папір \nЩоб завершити гру введіть 'exit' \nВведіть свою фігуру (stone, scissor, paper) : ").lower()
		if user_choise == "exit":
			print("Гру завершено.")
			break
		elif user_choise not in options:
			print("Некоректне значення! Оберіть stone, scissor або paper.")
			continue
		else:
			computer_choice = random.choice(options)
			print(f"Фігура комп'ютера: {computer_choice}")
			game(user_choise, computer_choice)
			continue
main()