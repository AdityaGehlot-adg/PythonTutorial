# implementing stack using list

s=[]
def push(ele):
    s.append(ele)
    print(s)

def pop_element():
    if(len(s)==0):
        print("stack is alreaady empty\n")
        print(s)
    else:
        s.pop()
        print(s)    

while(True):
    hit=int(input("which operation would you like to perform on stack \n 1.Push\n 2.Pop\n 3.Quit\n "))

    if(hit==1):
         if(len(s)==5):
            print("stack is full")
         else:     
            ele=int(input("enter the value you want to push\n"))
            push(ele)

    elif(hit==2):
            if(len(s)==0):
                print("stack is empty")
            else:
                pop_element()
            
    elif(hit==3):
         break

    else:
         print("choose the correct option")                   