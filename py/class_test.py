class Calculator:
    name='Good calculator'
    price=18
    def add(self,x,y):
        print(self.name)
        result=x+y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
cal = Calculator()

# print(cal.name)
print(cal.add(1,1))
