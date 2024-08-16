s=[]

class Enqueue:
    def rear_enqueue(self,ele):
        s.append(ele) 
        print(s)

    def front_enqueue(self,ele):
        s.insert(0,ele)
        print(s)

class Dequeue:
    def rear_dequeue(self):
        s.pop()
        print(s)
         
    def fornt_dequeue(self):
        s.pop(0)
        print(s)
                    

enq=Enqueue()
dque=Dequeue()

while(True):
    hit=int(input("which operation do you want to perform \n 1.enqueue\n 2.dequeue\n 3.quit\n "))
     
    

    
    if(hit==1): 
        if(len(s)==0):
            ele=int(input("enter the element you want to insert\n"))
            s.append(ele) 
            print(s)

        else:    
            side=int(input("from which end did you insernt an element \n 1.Rear\n 2.front\n"))

            if(side==1):
                ele=int(input("enter the element you want to insert\n"))
                enq.rear_enqueue(ele)

            elif(side==2):
                ele=int(input("enter the element you want to insert\n"))
                enq.front_enqueue(ele)

            else:
                print("choose correct option\n")    

    elif(hit==2):
        if(len(s)==0):
            print("Queue is aleady empty\n")
        
        elif(len(s)==1):
            s.pop()
            print(s)

        else:     
            side=int(input("from which end did you delete an element \n 1.Rear\n 2.front\n"))
            if(side==1):
                dque.rear_dequeue() 

            elif(side==2):
                dque.fornt_dequeue()  

            else:
                print("choose correct option\n")   

    elif(hit==3):
        break

    else:
        print("choose correct option\n")   
