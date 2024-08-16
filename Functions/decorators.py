def my_decorator(show):

    def show2():
        print("hii")
        show()
        print("aditya")

    return show2

@my_decorator
def show():
    print("hello")




show()