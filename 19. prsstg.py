# How to Parse a String to a Float or Integer using Python Code

# parse string into integer
string="12345"
print(type(string))
int_str=int(string)
print(int_str,"->",type(int_str))

# parse string into float
string="12.0678943"
print(type(string))
flt_str=float(string)
print(flt_str,"->",type(flt_str))

# parse string float numerial into integer 
string="9.00053"
print(type(string))
flt_str=float(string)
int_str=int(flt_str)  # we can also do int(float(string))
print(int_str,"->",type(int_str))
