# write a python program which calculate the sum of the numbers present in the list?

l=[2,5,1,9,2,7]

def cal_sum(l):
     
    sum=0
    for i in l:
        sum=sum+i
    return sum
    
add=cal_sum(l)
print(add)



# OR


# def cal_sum(l):
#     return sum(l)
    
# add=cal_sum(l)
# print(add)


