import pytest
from student import Stud
from list import List
from file import File

@pytest.fixture
def student_list():
    return List()

def test_add_student(student_list):
    s1 = Stud("Ivan", "Petrenko", "123", "ivan@mail")
    student_list.add_student(s1)
    
    assert len(student_list.students) == 1
    assert student_list.students[0].name == "Ivan"

def test_add_student_sorting(student_list):
    s1 = Stud("Zara", "A", "1", "1")
    s2 = Stud("Andriy", "B", "2", "2")
    
    student_list.add_student(s1)
    student_list.add_student(s2)

    assert student_list.students[0].name == "Andriy"
    assert student_list.students[1].name == "Zara"

def test_delete_student(student_list):
    s1 = Stud("Oleg", "D", "1", "e")
    student_list.add_student(s1)
    
    student_list.delete_student("Oleg")
    assert len(student_list.students) == 0

def test_delete_non_existent(student_list):
    s1 = Stud("Oleg", "D", "1", "e")
    student_list.add_student(s1)
    
    student_list.delete_student("NotOleg")
    assert len(student_list.students) == 1

def test_update_student(student_list):
    s1 = Stud("Taras", "Old", "000", "mail")
    student_list.add_student(s1)
    
    s_new = Stud("Taras", "NewSurname", "000", "mail")
    student_list.update_student("Taras", s_new)

    assert len(student_list.students) == 1
    assert student_list.students[0].surname == "NewSurname"

def test_update_student_resorting(student_list):
    s1 = Stud("Anna", "X", "1", "1")
    s2 = Stud("Boris", "Y", "2", "2")
    student_list.add_student(s1)
    student_list.add_student(s2)

    s_updated = Stud("Zlatan", "X", "1", "1")
    student_list.update_student("Anna", s_updated)
    
    assert student_list.students[0].name == "Boris"
    assert student_list.students[1].name == "Zlatan"

def test_file_save_load(tmp_path):
    file_path = tmp_path / "test_data.csv"
    fm = File(str(file_path))
    sl = List()
    
    s1 = Stud("TestUser", "S", "1", "e")
    sl.add_student(s1)
    
    fm.save_data(sl.get_all_students())
    
    new_sl = List()
    loaded_students = fm.load_data()
    for s in loaded_students:
        new_sl.add_student(s)
        
    assert len(new_sl.students) == 1
    assert new_sl.students[0].name == "TestUser"