class MathOper:
    def add(self, a, b):
        return a + b
    
    def subt(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b
    
    def div(self, a, b):
        try:
             return a / b
        except ZeroDivisionError:
            return ("Помилка ділення на 0 неможливе!")