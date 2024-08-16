# in priority queue based on the priority we can delete the element weather it is low to high precidence or high to low.  the priority is always on the deletion operation.

s=[]

def enqueue(ele):
    s.append(ele) 
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
            print("Queue is empty\n")

        elif(len(s)==1):
            s.pop()
            print(s)

        else:
            priority=int(input("In which priority you want to remove the element \n 1.Low to high\n 2.High to low\n "))  

            if(priority==1):
                s.sort()
                s.pop(0)
                print(s)

            elif(priority==2):
                s.sort()
                s.pop()
                print(s)    
    elif(hit==3):
        break

    else:
        print("choose correct option\n")              
