# second largest number in the string
l=[1,2,3,4,5,6,8,4,4,4,5,7,5,4,10,4,5,8,8,5,]

s=set(l)
l=list(s)
l.sort()
print(l[-2])

print(l)