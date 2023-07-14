n=int(input("Enter the Number:"))

result=list(map(lambda x : 2 ** x, range(n+1)))
print(result)

for i in range(0,n+1):
    print("Values of 2 raised to power of",i,"is",result[i])