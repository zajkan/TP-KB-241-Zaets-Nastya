
from functions import MathOper

class Oper:
    def __init__(self):
        self.oper = MathOper()
     	
    def perform_operation(self, a, b, oper):
        if oper == '+':
          return self.oper.add(a, b)
        elif oper == '-':
            return self.oper.subt(a, b)
        elif oper == '*':
           return self.oper.multi(a, b)
        elif oper == '/':
            return self.oper.div(a, b)
        if oper not in ['+', '-', '*', '/']:
            error_msg = "Невідома операція!\n"
            print(error_msg)
        