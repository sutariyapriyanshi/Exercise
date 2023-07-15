a="Hello I am Priyanshi Sutariya How are you ?"
w=a.split(" ")
print(w)
for i in range(len(w)):
    w[i]=w[i].lower()    # if i=0 then it is (hello) and it is convert w[i] means (Hello to hello) to lower
print(w)
w.sort()
print(w)

for i in w:
    print(i)
