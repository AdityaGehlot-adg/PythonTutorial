# Fibonacci Sequence

n=int(input("Enter a number\n"))
def feb(i):
     if(i==0 or i==1):
          print(0 and 1)
     print(feb(i)+feb(i-1))
          


for i in range(n):
    feb(i)

    