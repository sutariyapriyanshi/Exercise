# How to Check if a String is a Valid Keyword or Not
import keyword

words=['break','int','john','str','priyanshi','if','elif','else if','import','py','hello','python','do','keyword','three','lambda','continue','global']

for i in range(len(words)):
    if (keyword.iskeyword(words[i])):
        print(words[i],"is a keyword in python")
    else:
        print(words[i],"is not a keyword in python")

print(keyword.kwlist)
