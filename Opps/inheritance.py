class parent:
    def __init__(self):
        print("this is parent class constuctor")
    x=5
    def show(self):
        print("this is a parent class show")

    def demo(self):
        print("this is demo of parent class")    

class Child(parent):
    def __init__(self) -> None:
        super().__init__()
        print("this is child class constuctor")
    y=10
    def show(self):
        
        print("this is a child class show")

c=Child()
 
    