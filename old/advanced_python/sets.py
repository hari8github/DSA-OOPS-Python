# sets - unordered, mutable, no duplicates

myset = {1, 2, 3}
print(type(myset))

myset2 = set("hello")
print(myset2)

summa = set()

summa.add(1)
summa.add(2)
summa.add(3)

summa.discard(2)
#summa.clear()

for i in summa:
    print(i)

print(summa)

#union and intersection

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

d = odds.difference(primes)
print(d)

sym = odds.symmetric_difference(primes)
print(sym)

odds.update(primes)
print(odds)

print(odds.issubset(primes))
print(primes.issubset(odds))

print(odds.issuperset(primes))
print(primes.issuperset(odds))

setA = {1,2,3,4,5,6,7}

setB = setA
setB.add(89)

print(setB)
print(setA)