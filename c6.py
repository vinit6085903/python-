import math as p 
class Circle:
    def __init__(self,radis):
        self.radis=radis
    def circlr_area(self):
        return p.pi*radis*radis
    def circle_pre(self):
        return 2*p.pi*radis
radis=4
obj=Circle(radis)
a=obj.circle_pre();
b=obj.circlr_area();
print(a)
print(b)