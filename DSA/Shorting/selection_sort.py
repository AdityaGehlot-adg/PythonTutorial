l=[4,2,7,5,1,9,12,45,6]

for i in range(len(l)):
    min=i
    for j in range(i+1,len(l)):
        if(l[min]>l[j]):
            min=j

    l[i],l[min]=l[min],l[i]
print(l)

         
            
            
 
