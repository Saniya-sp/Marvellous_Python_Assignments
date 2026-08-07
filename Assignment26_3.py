"""WAP to implement a class named Arithmetic with the following specifications
The class should contain two instance variables:Value1 and Value2
Define a constructor (__init__) that initializes all instance variables to 0
Implement instance methods:
    -Accept()- accept values for Value1 and Value2 from user
    -Addition- return addition of Value1 and Value2
    -Subtraction- return subtraction of Value1 and Value2
    -Multiplication- return Multiplication of Value1 and Value2
    -Division- return Division of Value1 and Value2
    
Create multiple objects of the Arithmetic class and invoke all the instance methods for each object.

"""

class Arithmetic:
    # Value1 = 0
    # Value2 = 0

    def __init__(self):

        self.Value1 = 0
        self.Value2 = 0
        self.Sum = 0
        self.Sub = 0
        self.Mult = 0
        self.Div = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))

    def Addition(self):
        self.Sum = self.Value1 + self.Value2

    def Subtraction(self):
        self.Sub = self.Value1 - self.Value2

    def Multiplication(self):
        self.Mult = self.Value1 * self.Value2

    def Division(self):
        self.Div = self.Value1 / self.Value2
       
    def Display(self):
        print('Sum = ',self.Sum)
        print('Sub = ',self.Sub)
        print('Div = ',self.Div)
        print('Mult = ',self.Mult)
        

Obj1 = Arithmetic()

Obj1.Accept()
Obj1.Addition()
Obj1.Subtraction()
Obj1.Multiplication()
Obj1.Division()
Obj1.Display()

Obj2 = Arithmetic()

Obj2.Accept()
Obj2.Addition()
Obj2.Subtraction()
Obj2.Multiplication()
Obj2.Division()
Obj2.Display()
