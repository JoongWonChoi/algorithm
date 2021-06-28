
###Python simple function 사용 복습!###

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x},{self.y})"
p = Point(1,2)
print(p)
s = str(p)
print(s)




