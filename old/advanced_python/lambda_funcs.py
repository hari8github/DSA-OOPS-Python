"""add10 = lambda x:x+10
print(add10(5))

mul = lambda x,y : x*y
print(mul(45,45))"""

"""points2d = [(1,2), (15,1), (5,-1), (10,4)]
points2d_sorted = sorted(points2d)

print(points2d)
print(points2d_sorted)

points2d_sort_index = sorted(points2d, key = lambda x: x[1])
print(points2d_sort_index)"""

# map (func, variable)

"""a = [1,2,3,4,5,6,7,8,9]
b = map(lambda x: x**2, a)
#print(b) creates an object so we want to use list. 
print(list(b))

c = [x**2 for x in a]
print(c)"""

# filter

"""a = [1,2,3,4,5,6,7,8,9]
b = filter(lambda x: x%2!=0, a)
print(list(b))"""

# reduce

from functools import reduce
a = [1,2,3,4,5]

product_a = reduce(lambda x,y :x*y, a)
print(product_a)