#substraction of to tuple using class
class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
    def __str__(self):
        return "(%d,%d)"%(self.x, self.y)
    def __sub__(self, p2):
        p3=Point()
        p3.x=self.x-p2.x
        p3.y=self.y-p2.y
        return p3
p1=Point(10,20)
p2=Point(1,1)
print("P1 is:",p1)
print("P2 is:",p2)
p4=p1-p2
print("substraction is:",p4)