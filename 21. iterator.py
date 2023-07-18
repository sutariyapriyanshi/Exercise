# nums=[1,2,3,4,5,6]

# for i in nums:
#     print(i)
# print("\n")

# iterate=iter(nums)
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print("\n")

# string="Hello Priyanshi"
# for i in string:
#     print(i)
# print("\n")

# iterate=iter(string)
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(next(iterate))

class Fantasticfive:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if (self.num <=5):
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
        
obj=Fantasticfive()
for i in obj:
    print(i)
