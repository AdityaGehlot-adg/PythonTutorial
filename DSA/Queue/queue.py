s=[]


def enqueue(ele):
    s.append(ele) 
    print(s) 

def dequeue():
    a=s.pop(0) 
    print("element removed :"+str(a))
    print(s)            
          
while(True):
    hit=int(input("which operation do you want to perform \n 1.enqueue\n 2.dequeue\n 3.quit\n "))
    if(hit==1):
        if(len(s)==5):
            print("queue is full \n")
        else:    
            ele=int(input("enter the element you want to insert\n"))
            enqueue(ele)

    elif(hit==2):
        if(len(s)==0):
            print("Queue is already empty\n")
        else:
            dequeue()    
    
    elif(hit==3):
        break

    elif(hit!=[1,2,3]):
        print("enter valid choice")



    