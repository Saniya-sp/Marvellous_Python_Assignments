"""WAP to implement a class named BankAccount with the following specifications
The class should contain two instance variables:
    -Name(account holder name)
    -Amount(account balance)
The class should contain one class variable
    -ROI(Rate Of Interest -initialize to 10.5)
Define a constructor (__init__) that accepts Name and initial Amount
Implement following instance methods:
    -Display()- displays account holder name and current balance
    -Deposite()- accepts an amount from the user and adds it to balance
    -Withdrawl()- accepts an amount from the user and substracts it from balance
        (Ensure withdrwal is allowed only when sufficient balance exixsts)
    -CalculateInterest()- calculates and returns interest using formula:
        Interest = (ROI * Amount) / 100

CReate multiple objects and demonstrate all methods
    """

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):

        self.Name = Name
        self.Amount = Amount
        self.Balance = self.Amount

    def Display(self):
        print(f"Acoount Holder Name: {self.Name}, Balance: {self.Amount}")
        
    def Deposite(self):
        amount_to_deposit = int(input("Enter amount to deposite in account:"))
        self.Amount = self.Amount + amount_to_deposit
        print(f"--* Amount deposited successfully. Current balance is: {self.Amount} *--") 


    def Withdrawl(self):
        amount_to_withdrawl = int(input("Enter amount to withdrawl from account:"))

        if self.Amount > amount_to_withdrawl:            
            self.Amount = self.Amount - amount_to_withdrawl
            print(f"--* Amount withdrawled successfully. Current balance is: {self.Amount} *--") 

        else:
            print("--? Withdrawl failed. Insuficiant account balance. ?--") 
            
    def CalculateInterest(self):
        return (self.ROI * self.Amount) / 100
        # print(self.Amount)
    
Obj1 = BankAccount("Saniya Pathan", 1000)
Obj1.Display()
Obj1.Deposite()
Obj1.Withdrawl()
print("Interest is: ", Obj1.CalculateInterest())