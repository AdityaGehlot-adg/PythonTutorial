def odd_no(n):
    i=1
    while i<n:
        yield i
        i+=1

no=odd_no(10)       
print(next(no))
print(next(no))
# print(next(no))
# print(next(no))