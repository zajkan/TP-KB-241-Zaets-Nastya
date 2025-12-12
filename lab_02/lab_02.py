from sys import argv 
import csv

list = []

def loadCSV():
    global filename
    filename = "lab2.csv"
    if len(argv) > 1:
        filename = argv[1]

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file, skipinitialspace=True)
            for row in reader:
                list.append({
                    "name": row["StudentName"],
                    "surname": row["StudentSurname"],
                    "phone": row["StudentPhone"],
                    "email": row["StudentEmail"]
                })
    except FileNotFoundError:
        print("Файл не знайдено, починаємо з порожнім списком.")
    except KeyError as e:
        print(f"Помилка структури CSV: {e}")

def addNewElement():
    name = input("Будь ласка, введіть ім'я студента: ")
    surname = input("Будь ласка, введіть прізвище студента: ")
    phone = input("Будь ласка, введіть номер телефону студента: ")
    email = input("Будь ласка, введіть email студента: ")
    newItem = {"name": name, "surname": surname, "phone": phone, "email":email}

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("Новий студент був додан")
    return

def deleteElement():
    name = input("Будь ласка, введіть ім'я студента для видалення: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Студент не був знайден")
    else:
        print("Видалення " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
   name = input("Будь ласка, введіть ім'я студента для оновлення: ")
   found = None
   for item in list:
      if item["name"] == name:
            found = item
            break

   if not found:
        print("Студент не був знайден")
        return

   print(f"Оновлення студента: {found['name']} {found['surname']}")

   new_name = input(f"Введіть нове ім'я [{found['name']}]: ") or found['name']
   new_surname = input(f"Введіть нове прізвище [{found['surname']}]: ") or found['surname']
   new_phone = input(f"Введіть новий номер телефону [{found['phone']}]: ") or found['phone']
   new_email = input(f"Введіть нову email [{found['email']}]: ") or found['email']
    
   list.remove(found)

   updatedItem = {"name": new_name, "surname": new_surname, "phone": new_phone, "email": new_email}

   insertPosition = 0
   for item in list:
      if new_name > item["name"]:
            insertPosition += 1
      else:
            break
   list.insert(insertPosition, updatedItem)

   print("Студент був оновленний")
   return

def saveList():
    with open(filename, "w") as file:
        fieldnames = ["StudentName", "StudentSurname", "StudentPhone", "StudentEmail"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for student in list:
            writer.writerow({
               "StudentName": student['name'],
               "StudentSurname": student['surname'],
               "StudentPhone": student['phone'],
				   "StudentEmail": student['email'],
				})
    print(f"Дані збережено в {filename}")

def printAllList():
    for student in list:
        print(f"{student['name']} {student['surname']} | {student['phone']} | {student['email']}")      

def main():
    loadCSV()
    
    while True:
        chouse = input("\nБудь ласка, оберіть дію [ C створення, U оновлення, D видалення, P показати список,  X Вихід ] ")
        match chouse:
            case "C" | "c":
                print("Новий студент буде додано:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Дані студента будуть оновленно")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Студента буде видалено")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("Список студентів буде надруковано")
                printAllList()
            case "X" | "x":
                print("Вихід")
                saveList()
                break
            case _:
                print("Невідома дія")

if __name__ == "__main__":
    main()