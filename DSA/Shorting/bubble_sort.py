l=[2,4,1,7,9,48,44,6,1]

for i in range(len(l)-1):
     for j in range(i+1,len(l)):
          
         if(l[i]>l[j]):
              temp=l[i]
              l[i]=l[j]
              l[j]=temp
              print(l)
