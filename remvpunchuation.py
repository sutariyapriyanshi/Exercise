# Write a program to remove punctuations from the string

# punctuations "" ' ' , . / ? \ | {} [] () < > ! ~ ` ` 

punc='''/?<>';:{\}"".,[]!~`@#$%^&*()|'''
string=input("Enter any string: ")
emptystring=""
for i in string:
    if (i not in punc):
        emptystring=emptystring+i

print(emptystring)