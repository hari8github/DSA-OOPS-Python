# tuples - ordered, immutable and allows duplicate elements

mytuple = ("hari")
print(type(mytuple)) # string

tuple2 = ("hari", )
print(type(tuple2)) # tuple, wierd but yes.

summa = tuple(["maths", "science", "social science"])
print(summa)
print(summa[1])

for i in summa:
    print(i)

print(len(summa))
print(summa.count("maths"))

# same as lists, but a tuple is not editable (immutable)

my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print (name)
print(age)
print(city)

my_tuple2 = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple2

print(i1)
print(i3)
print(i2)

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes") # 104 bytes
print(sys.getsizeof(my_tuple), "bytes") # 80 bytes