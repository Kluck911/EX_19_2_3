class Calculator:
    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def subtraction(self, x, y):
        return x - y

    def adding(self, x, y):
        return x + y

a = Calculator()
print(a.multiply(2, 4))
'''
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y

    def subtraction(self):
        return self.x - self.y

    def adding(self):
        return self.x + self.y
        
        


a = Calculator(2, 3)
print(a.multiply())

'''




