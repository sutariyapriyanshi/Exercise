# def my_gen():
#     yield 1 # for generator we use yield
#     yield 10
#     return 2 
# # yield is like return it is used to take object we can't take values until and unless we use next function. 

# obj=my_gen()
# print(obj) # used for object

# print(obj.__next__()) # used to return value
# print(obj.__next__()) 


def func(n):
    a=0
    while (a<n):
        if(a%2==0):
            yield a
        a+=1
x=func(12)
for i in x:
    print(i)
