class Arithmetic:

    def __init__(self,value1,value2):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first value:"))
        self.value2 = int(input("Enter second value:"))
        return self.value1,self.value2

    def Addition(self):
         res = self.value1 + self.value2
         return res

    def Substracttion(self):
         res = self.value1 - self.value2
         return res

    def Multiplication(self):
         res = self.value1 * self.value2
         return res

    def Division(self):
         res = self.value1 / self.value2
         return res

def main():
    Obj1 = Arithmetic(0,0)
    Obj1.Accept()
    print("Addition of two numbers is:", Obj1.Addition())
    print("Substraction of two numbers is:", Obj1.Substracttion())
    print("Multiplication of two numbers is:", Obj1.Multiplication())
    print("Division of two numbers is:", Obj1.Division())

if __name__ == "__main__":
    main();