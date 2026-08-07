"""WAP to implement a class named Numbers with the following specifications
The class should contain one instance variables:
    -Value
Define a constructor (__init__) that accepts number from the user and initializes Value
Implement following instance methods:
    -ChkPrime()- return True if number is prime, else return False
    -ChkPerfect()- return True if number is perfect, else return False
    -Factors()- display all factors of the number
    -SumFactors()- return the sum of all factors

CReate multiple objects and demonstrate all methods
    """

class Numbers:
    
    def __init__(self):

        self.Value = int(input("Enter a number: "))
        # self.Amount = Amount
        # self.Balance = self.Amount

    def ChkPrime(self):
        if self.Value == 2:
            return True
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
            
        return True
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i

        return sum == self.Value


    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors
        
    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i

        return sum

                
Obj1 = Numbers()
print(Obj1.ChkPrime())
print(Obj1.ChkPerfect())
print(Obj1.Factors())
print(Obj1.SumFactors())

Obj2 = Numbers()
print("Is prime number:",Obj2.ChkPrime())
print("Is perfect number:",Obj2.ChkPerfect())
print("Factors are: ",Obj2.Factors())
print("SUm of factors is:",Obj2.SumFactors())
