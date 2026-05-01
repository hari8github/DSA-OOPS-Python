#collections - counter, namedtuple, orderedDict, deque

from collections import Counter
a = "aaaaaannnnnnncc"
b=Counter(a)
print(b.items())

print(b.keys())
print(b.values())
print(b.most_common(1))
print(list(b.elements()))

