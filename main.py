print ("**********************************************************")
class Circle :
    def  __init__(self,width, height):
        self.width=width
        self.height=height
        x=width*height
        

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2* (self.width +self.height)
    
r1=Circle(10,20)
print("the area of this is : ",r1.area())
print("the perimeter(of this is : ",r1.perimeter())
print(str(r1))
