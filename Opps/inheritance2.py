class Rectangle:
    l=10
    w=15
    def show(self):
        print("rectangle") 
    def cal_area(self):
        return self.l*self.w
    
class Cuboid(Rectangle):
    h=20

    def show(self):
        l=super().l
        print("cuboid" +str(l))

    def cal_vol(self):
        l=super().l
        w=super().w
        return l*w*self.h
    
cu=Cuboid()
print(cu.cal_vol()) 
print(cu.cal_area()) 
cu.show()  
