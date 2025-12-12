from student import Stud

class List:
    def __init__(self):
        self.students = []

    def add_student(self, student: Stud):
        insert_position = 0
        for item in self.students:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        print("Новий студент був додан")

    def delete_student(self, name):
        for item in self.students:
            if item.name == name:
                self.students.remove(item)
                print(f"Студент {name} був видалений")
                return
        print("Студент не був знайден")

    def find_student(self, name):
        for item in self.students:
            if item.name == name:
                return item
        return None

    def update_student(self, old_name, new_student: Stud):
        student_to_remove = self.find_student(old_name)
        if student_to_remove:
            self.students.remove(student_to_remove)
            self.add_student(new_student) 
            print("Студент був оновленний")
        else:
            print("Студент не був знайден")

    def get_all_students(self):
        return self.students

    def print_all(self):
        for student in self.students:
            print(student)