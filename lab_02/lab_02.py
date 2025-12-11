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
    name = input("Pease enter student name: ")
    surname = input("Pease enter student surname: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    newItem = {"name": name, "surname": surname, "phone": phone, "email":email}

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
   name = input("Please enter name to be updated: ")
   found = None
   for item in list:
      if item["name"] == name:
            found = item
            break

   if not found:
        print("Student not found")
        return

   print(f"Updating student: {found['name']} {found['surname']}")

   new_name = input(f"Enter new name [{found['name']}]: ") or found['name']
   new_surname = input(f"Enter new surname [{found['surname']}]: ") or found['surname']
   new_phone = input(f"Enter new phone [{found['phone']}]: ") or found['phone']
   new_email = input(f"Enter new email [{found['email']}]: ") or found['email']
    
   list.remove(found)

   updatedItem = {"name": new_name, "surname": new_surname, "phone": new_phone, "email": new_email}

   insertPosition = 0
   for item in list:
      if new_name > item["name"]:
            insertPosition += 1
      else:
            break
   list.insert(insertPosition, updatedItem)

   print("Student has been updated")
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
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                saveList()
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()