import pytest
import lab_02

@pytest.fixture(autouse=True)
def clean_list():
    lab_02.list = []
    yield
    lab_02.list = []

def test_add_new_element(monkeypatch):
    inputs = iter(["Ivan", "Petrenko", "12345", "ivan@mail.com"])
    
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    lab_02.addNewElement()

    assert len(lab_02.list) == 1
    assert lab_02.list[0]['name'] == "Ivan"
    assert lab_02.list[0]['surname'] == "Petrenko"

def test_add_element_sorting(monkeypatch):
    inputs1 = iter(["Zara", "A", "1", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs1))
    lab_02.addNewElement()

    inputs2 = iter(["Andriy", "B", "2", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs2))
    lab_02.addNewElement()

    assert lab_02.list[0]['name'] == "Andriy"
    assert lab_02.list[1]['name'] == "Zara"


def test_delete_element(monkeypatch):
    lab_02.list.append({"name": "Oleg", "surname": "D", "phone": "1", "email": "e"})
    
    monkeypatch.setattr('builtins.input', lambda _: "Oleg")
    lab_02.deleteElement()
    
    assert len(lab_02.list) == 0

def test_update_element(monkeypatch):
    lab_02.list.append({"name": "Taras", "surname": "Old", "phone": "000", "email": "student@mail"})

    inputs = iter(["Taras", "", "NewSurname", "", ""])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    lab_02.updateElement()

    assert lab_02.list[0]['surname'] == "NewSurname"
    assert lab_02.list[0]['name'] == "Taras" 


def test_save_list():
    lab_02.list = [{"name": "TestUser", "surname": "S", "phone": "1", "email": "e"}]
    lab_02.filename = "test_output.csv"

    lab_02.saveList()

    with open("test_output.csv", "r") as f:
        content = f.read()
        assert "TestUser" in content
        assert "StudentName" in content