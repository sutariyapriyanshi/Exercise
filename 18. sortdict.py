marks={"Lisa":97,"Peter":95,"Phena":90,"Vidhya":94}
print(marks)
# sorting based on values
sortvalues=sorted(marks.items(), key= lambda x : x[1])
print(sortvalues)

# Based on key values
sortvalues=sorted(marks.items(), key= lambda x : x[0])
print(sortvalues)

# Sort only with values
b=sorted(marks.values())
print(b)

# Sort only with keys
c=sorted(marks.keys())
print(c)
