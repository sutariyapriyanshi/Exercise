l=['priyanshi','Sutariya','delu','minu','sujal']

for i in l:
    print(i.upper())

newlist=[i.upper() for i in l]
print(newlist)

m=[i for i in range(0,11)]
print(m)
k=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # using manuallly
empty=[]
for i in k:
    if(i%2==0):
        empty.append(i)

print(empty)

a=[i for i in range(11) if i%2==0 ] # list comprehension
print(a)