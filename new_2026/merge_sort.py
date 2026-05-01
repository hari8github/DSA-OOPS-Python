def merge_sort(list):
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            l.append(left[i])
            i += 1
        else: 
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)
    
    if n <= 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

oru_list = [1, 10, 20, 48, 33, 3, 22, 24, 6, 4, 2005, 2004]
l = merge_sort(oru_list)
print(verify_sorted(oru_list))
print(verify_sorted(l))
print(l)