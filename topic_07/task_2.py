class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"

students = [
    Student("Ксенія", 21),
    Student("Ярослав", 19),
    Student("Павло", 22),
    Student("Ангеліна", 20)
]

def main():
	sort_age = sorted(students, key=lambda student: student.age)

	print("Сортування за віком по зростанню ")
	for student in sort_age:
		print(student)


	sort_name = sorted(students, key=lambda student: student.name)

	print("\nСортування за ім'ям по алфавіту")
	for student in sort_name:
         print(student)

main()