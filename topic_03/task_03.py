print("Тестування функцій словників\n")
test_dict = {'name':'Kate', 'age':17, 'city':'Kyiv'}
print("Початковий словник:", test_dict)
test_dict.update({'age': 18, 'country': 'Ukraine'})
print("update({'age': 18, 'country': 'Ukraine'}):", test_dict)
print("keys():", list(test_dict.keys()))
print("values():", list(test_dict.values()))
print("items():", list(test_dict.items()))
del test_dict['city']
print("del test_dict['city']:", test_dict)
test_dict.clear()
print("clear():", test_dict)