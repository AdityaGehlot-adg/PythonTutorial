class first:
    def __init__(self,name,roll_no) -> None:
        self.name=name
        self.roll_no=roll_no
        print("object initialized")

    def show(self,age):
        print("your name is " +self.name +" and age is " + str(age))    

obj=first("aditya",157)

# d={"name":"ankit","surname":"gehlot","roll no":"003","name":["aditya",2,3]}

# print(d["name"])
# a=[]
# print(type(a))
# 
# class veichle:
#     st="toyoto"
#     def met1(self):
#         print("toyoto is a car")
#     def met1(self,name):
#         self.name=name    
#         print("my name is "+name)
#     def __init__(self,car):
#         self.car=car
#         print("this is a defalt constructor " +car) 
# vi=veichle("hundai") 
# vi.met1("nehu")