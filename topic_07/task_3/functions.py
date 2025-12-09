class MathOper:
    def add(self, a, b):
        return a + b
    
    def subt(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError ("Помилка ділення на 0 неможливе!")