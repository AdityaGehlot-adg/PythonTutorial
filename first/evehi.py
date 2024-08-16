l=[2,7,3,0,9,6,1]

for i in range(len(l)-1):
    k=l[i]
    for j in range(1,len(l)):
        if(k>l[j]):
            k,l[j]=l[j],k

print(l)            








# l=[10,20,30,40,50,60]

# k=[i>20 for i in l]
# print(k)


# l=[1,2,3,4,5,6,7,9,8,5,1,1,4,5,5]

# i=0
# while(i< len(l)):
#     print(l[i])
#     i+=1

# else:
#     print("task completed\n")    






# k=map(lambda l:l**2,)
# print(k)
# # k=[10,20,30,40]
# # new=[]
# def cube(item):
#     return item*item*item

# new=list(map(cube,l))
# print(new)











# # SUM OF DIGITS
# def sum_of_digits(j):
#     while j!=0:
       
#          k=j%10






# LARGEST NUMBER IN THE LIST
# l=[1,5,3,7,2,8,7,6,9]



# def largest(l):
#     s=set(l)
#     l=list(s)
#     l.sort()
#     return l[-2]

# k=largest(l)
# print(k)






# FEBBIBOCI SERIES  
# def febbi(n):
#     if()







# # fACTORIAL OF A NUMBER
# def fact(a):
#     if(a==0):
#         return 1
#     else:
#         return a*fact(a-1)


# k=fact(5)
# print(k)








# # CHECK NUMBER IS PRIME OR NOT
# def check_no(a):
#     if(a%2==0):
#         return "no is prime"
#     else:
#         return "no is not prime"   

# k=check_no(11)        
# print(k)






# #REVERSE A STRING
# def fun(s):
#     return s[::-1]

# k=fun("Aditya")
# print(k)






# TRY EXCEPT BLOCK
# try:
#     x=int(input("enter a no\n"))

#     y=x+2
#     print(y)

# except:
#     print("enter a integer number")

# finally:
#     print("you learned")       
