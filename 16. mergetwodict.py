# Using bar(|) operator
d1={"John":98,"Lisa":97}
d2={"Lisa":97,"Peter":95}
print(d1 | d2)

# Using kwargs (**) operator
d4={"John":98,"Lisa":97,"Jena":92}
d3={"Lisa":97,"Peter":95,"Phena":90}
print({**d3,**d4})

# Using  Copy and update method
d5={"John":98,"Lisa":97,"Jena":92}
d6={"Lisa":97,"Peter":95,"Phena":90,"Vidhya":94}

d7=d6.copy()
d7.update(d5)
print(d7)
