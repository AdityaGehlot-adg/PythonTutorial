# Python program to interchange first and last elements in a list

l=[1,2,3,4,5,6,7,8,9,10]
# temp=l[0]
# l[0]=l[9]
# l[9]=temp

# or

# a,b=b,a
l[0],l[9]=l[9],l[0]
print(l)
