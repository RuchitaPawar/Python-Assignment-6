class Demo:
  Value = None

  def __init__(self,no1,no2):
     self.no1 = no1
     self.no2 = no2

  def Fun(self,no1,no2):
      print("Inside Fun");
      print("First variable:",no1);
      print("Second variable:", no2);

  def Gun(self, no1, no2):
       print("Inside Gun");
       print("First variable:", no1);
       print("Second variable:", no2);

def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))

    Obj1.Fun(num1,num2)
    Obj1.Gun(num1,num2)

    Obj2.Fun(num1,num2)
    Obj2.Gun(num1,num2)

if __name__ == "__main__":
 main();