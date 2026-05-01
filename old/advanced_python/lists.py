#lists - ordered, mutable and allows duplicates

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True]
print(mylist2)

item = mylist[1]
print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")

else:
    print("no")

print(len(mylist))

mylist.append("tomato")
print(mylist)

mylist.insert(1, "strawberry")
print(mylist[1])

a = mylist.pop()
print(a, mylist)

b = mylist.reverse()
print(mylist, b)

c = mylist.clear()
print(c,  mylist)

num = [3,4,56,8,54,7,4,2,1]
print(num)
d = num.sort() # if we use sort, it changes the list itself, so you can create a new variable and assign the list using SORTED.
print(num)

e = sorted(num)
print(e)

summa = [1] * 5
print(summa)

summa2 = [0] * 5

print(summa + summa2)

num = [3,4,56,8,54,7,4,2,1]
x = num[1:5]
print(x)

x = num[1:]
print(x)

x = num[:5]
print(x)

x = num[::2]
print(x)

fake = ["python", "is"]
original = fake
# here both the list gets appended with the word, if we use COPY() we can resolve it
original.append("good")
print(original)
print(fake) 

sq = [i**i for i in num]
print(num , "\n", sq)