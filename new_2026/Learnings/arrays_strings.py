new_list = [1,2,3]
new_list[2]
#new_list[5] # IndexError

# searching

if 2 in new_list:
    print("True")

for i in new_list:
    if i == 2:
        print("True it is there")
        break 

# inserting

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.append(5)
print(numbers)

numbers.pop()
print(numbers)

numbers.insert(3, 5)
print(numbers)

numbers[1] = 4
print(numbers)

# STRINGS

a = 'liverpool'
b = a+'fc'
print(b)

for i in a:
    if i == 'p':
        print("P is present")
        print(i.index)
        break