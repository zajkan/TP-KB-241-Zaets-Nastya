import csv
from student import Stud

class File:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        students = []
        try:
            with open(self.filename, "r", newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file, skipinitialspace=True)
                for row in reader:
                    student = Stud(
                        name=row["StudentName"],
                        surname=row["StudentSurname"],
                        phone=row["StudentPhone"],
                        email=row["StudentEmail"]
                    )
                    students.append(student)
        except FileNotFoundError:
            print("Файл не знайдено, починаємо з порожнім списком.")
        except KeyError as e:
            print(f"Помилка структури CSV: {e}")
        return students

    def save_data(self, student_list):
        with open(self.filename, "w", newline='', encoding='utf-8') as file:
            fieldnames = ["StudentName", "StudentSurname", "StudentPhone", "StudentEmail"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in student_list:
                writer.writerow({
                    "StudentName": student.name,
                    "StudentSurname": student.surname,
                    "StudentPhone": student.phone,
                    "StudentEmail": student.email,
                })
        print(f"Дані збережено в {self.filename}")