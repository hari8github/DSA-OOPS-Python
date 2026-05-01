# strings - orderred ,immutable, text representation

a = "hi"
b = "i'am hari"
c = 'i\'am hari'

print(a,b,c)

multi = """hari venkat \
venkat"""
multi2 = """hari venkat 
venkat"""
print(multi)
print(multi2)

my_string = "parama padi da"

char = my_string[1]

print(char)

char2 = my_string[-1]

print(char2)

char3 = my_string[1:4]
print(char3)

if 'a' in my_string:
    print("iruku")
else:
    print("else")

space = "               hi"
print(space)

print(space.strip())

print(my_string.find("parama"))
print(my_string.find("dei gopal"))

print(my_string.split())

loki = 'hi,da,loki'
mid_loki = loki.split(",")
new_loki = ''.join(mid_loki)
print(new_loki)

my_list = ['k'] * 99999
#print(my_list)

from timeit import default_timer as timer
from tracemalloc import stop
#bad
start = timer()
laptop = ''
for i in my_list:
    laptop += i
stop = timer()
#print(laptop)
print(stop - start)


#good
start2 = timer()
laptop2 = ''.join(my_list)
stop2 = timer()
#print(laptop2)
print(stop2 - start2)

#format
var = 3.12352345345

var2 = "the variable is {}".format(var)
print(var,var2)

var2 = "the variable is {:.2f}".format(var)
print(var,var2)