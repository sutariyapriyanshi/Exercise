# Count the Number of vowels in the word

# Using Dictionary
print("Using Dictionary")
a="Hello My name is Priyanshi I need Coffee right now"
vowels="aeiouAEIOU"
# a=a.casefold() it will transfer the whole string into lower case
count={}.fromkeys(vowels,0)  # it will create the dictionary like {a:0,e:0,i:0,o:0,u:0....like this}
print(count)
for char in a:
    if(char in count):
        count[char]+=1

print(count)

# Using list and dictionary comprehension
print("\nUsing list and dictionary comprehension")
a="Hello My name is Priyanshi I need Coffee right now"
vowels="aeiou"
a=a.casefold() 
count={key:sum([1 for char in a if char == key])for key in vowels}
print(count)

