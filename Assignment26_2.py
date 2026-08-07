"""WAP to implement a class named Circle with the following specifications
The class should contain three instance variables:Radius, Area and Circumference
The class should contain one class variable named PI, initialized to 3.14.
Define a constructor (__init__) that initializes all instance variables to 0.0
Implement instance methods:
    -Accept()- accept radius of circle from user
    -CalculateArea()- calculates the area of ciscle and stored it in Area variable
    -CalculateCircumference() - calculates the circumference of the circle and stored it in the Circumference variable
    -Display()- display the values of Radius, Area and Circumference

Create multiple objects of the Circle class and invoke all the instance methods for each object.

"""

class Circle:
    PI = 3.14

    def __init__(self):

        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input("Enter the radius of circle: "))

    def CalculateArea(self):
        self.Area = self.PI * self.Radius **2

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

        
    def Display(self):
        print('Area = ',self.Area)
        print('Circumference = ',self.Circumference)
 

Obj1 = Circle()
# Obj2 = Circle(51,101)

Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()
