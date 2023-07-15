# Using for loop
print("Number is divisible by 13 are")
for i in range(1,100):
    if (i % 13 == 0):
        print(i)

# Using anoynomous function (lambda function) and filter
l=[45,67,89,63,26,57,13,59,65,130,1]
result = list(filter(lambda x : x % 13 == 0,l))
print("The Number which is divisible by 13 is as below")
print(result)
