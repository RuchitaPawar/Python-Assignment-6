class Circle:
  PI = 3.14

  def __init__(self,Radius,Area,Circumference):
     self.Radius = 0.0
     self.Area = 0.0
     self.Circumference = 0.0

  def Accept(self):
      radius = int(input("Enter the radius of circle:"))
      self.Radius = radius
      return self.Radius

  def CalculateArea(self,radius):
      self.Area = self.PI * radius * radius
      return self.Area;

  def CalculateCircumference(self, radius):
      self.Circumference =  2 * self.PI * radius
      return self.Circumference;

  def Display(self,Radius,Area,Circumference):
      print("Radius of circle is: ",self.Radius)
      print("Area of circle is: ", self.Area)
      print("Circumference of circle is: ", self.Circumference)


def main():
    Obj1 = Circle(0,0,0);
    res = Obj1.Accept();
    Obj1.CalculateArea(res)
    Obj1.CalculateCircumference(res)
    Obj1.Display(Obj1.Radius,Obj1.Area,Obj1.Circumference)

if __name__ == "__main__":
 main();
