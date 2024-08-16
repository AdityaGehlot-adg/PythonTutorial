# map function is a higher order function which takes  function as a argument.

l=[1,2,3,4,5,6]

k=list(map(lambda l:l*7,l))
print(k)



# filter function is a higher order function which takes function as an argument and give the filter values.

l=[10,20,30,40,50,60]

k=list(filter(lambda l:l>20,l))
print(k)
