class Student:
#     name=None
#     m1=None
#     m2=None
#     m3=None
    def __init__(self,name,m1,m2,m3) -> None:
         self.name=name
         self.m1=m1
         self.m2=m2
         self.m3=m3
    def cal_average(self,m1,m2,m3,name):
         average=(m1+m2+m3)/3   
         print(name + " your 3 subject average is "+average)

m1=input("enter first subject marks")
m2=input("enter second subject marks")
m3=input("enter third subject marks")
name=input("enter your name")

s1=Student("Aditya",90,91,95)
s1.cal_average
del name
print(name)

