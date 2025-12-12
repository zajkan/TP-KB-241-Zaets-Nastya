import sys
from student import Stud
from list import List
from file import File

def main():
    filename = "lab3.csv"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file_man = File(filename)
    stud_list = List()
    
    loaded_data = file_man.load_data()
    for s in loaded_data:
        stud_list.add_student(s)

    while True:
        choice = input("Будь ласка, оберіть дію [ C створення, U оновлення, D видалення, P показати список,  X Вихід ]: ")
        match choice.lower():
            case "c":
                print("Новий студент буде додано:")
                name = input("Будь ласка, введіть ім'я студента: ")
                surname = input("Будь ласка, введіть прізвище студента: ")
                phone = input("Будь ласка, введіть номер телефону студента: ")
                email = input("Будь ласка, введіть email студента: ")
                new_student = Stud(name, surname, phone, email)
                stud_list.add_student(new_student)
                stud_list.print_all()
            
            case "u":
                print("Дані студента будуть оновленно")
                name = input("Будь ласка, введіть ім'я студента для оновлення: ")
                found = stud_list.find_student(name)
                
                if found:
                    print(f"Оновлення студента: {found}")
                    new_name = input(f"Введіть нове ім'я [{found.name}]: ") or found.name
                    new_surname = input(f"Введіть нове прізвище [{found.surname}]: ") or found.surname
                    new_phone = input(f"Введіть новий номер телефону [{found.phone}]: ") or found.phone
                    new_email = input(f"Введіть нову email [{found.email}]: ") or found.email
                    
                    updated_student = Stud(new_name, new_surname, new_phone, new_email)
                    stud_list.update_student(name, updated_student)
                    stud_list.print_all()
                else:
                    print("Студент не був знайден")

            case "d":
                print("Студента буде видалено")
                name = input("Будь ласка, введіть ім'я студента для видалення: ")
                stud_list.delete_student(name)
                stud_list.print_all()

            case "p":
                print("Список студентів буде надруковано")
                stud_list.print_all()

            case "x":
                print("Вихід")
                file_man.save_data(stud_list.get_all_students())
                break
            
            case _:
                print("Невідома дія")

if __name__ == "__main__":
    main()