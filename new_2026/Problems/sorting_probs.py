"""1) Given an array, sort it using bubble sort and count the number of swaps made."""
def bubble_sort(arr):
    counter = 0              # tracks number of swaps
    n = len(arr)
    flag = True              # controls outer loop — True means a swap occurred
    while flag:
        flag = False         # assume sorted until a swap happens
        for i in range(1, n):
            if arr[i-1] > arr[i]:        # adjacent elements out of order
                flag = True              # swap occurred — need another pass
                arr[i-1], arr[i] = arr[i], arr[i-1]  # swap
                counter += 1            # increment swap count
    return arr, counter

nums = [6,5,3,6,83,2,7,8,3,6,6,33545,678,0,2]
a = bubble_sort(nums)
(a)

"""2) Given a nearly sorted array (each element is at most k positions away from its sorted position), sort it efficiently."""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):           # start from index 1, treat left as sorted
        for j in range(i, 0, -1):   # move left from current position
            if arr[j-1] > arr[j]:   # element out of order
                arr[j-1], arr[j] = arr[j], arr[j-1]  # swap into correct position
            else:
                break
    return arr

nums = [3, 2, 1, 5, 4, 7, 6]
b = insertion_sort(nums)
(b)

"""3) Given two sorted arrays, merge them into one sorted array without using built-in sort."""

def merge_sort(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    tot_len = n1 + n2

    l, r = 0, 0                      # pointers for arr1 and arr2
    sorted_arr = [0] * tot_len        # result array
    i = 0                             # pointer for sorted_arr

    while l < n1 and r < n2:         # compare elements from both arrays
        if arr1[l] < arr2[r]:
            sorted_arr[i] = arr1[l]  # arr1 element is smaller
            l += 1
        else:
            sorted_arr[i] = arr2[r]  # arr2 element is smaller
            r += 1
        i += 1

    while l < n1:                    # remaining elements in arr1
        sorted_arr[i] = arr1[l]
        l += 1
        i += 1
    while r < n2:                    # remaining elements in arr2
        sorted_arr[i] = arr2[r]
        r += 1
        i += 1

    return sorted_arr

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

c = merge_sort(arr1, arr2)
(c)

"""4) Given an array, find the kth largest element using quick sort partitioning."""

def quick_sort(arr):
    if len(arr) <= 1:        # base case — single element is already sorted
        return arr
    pivot = arr[-1]          # choose last element as pivot

    L = [x for x in arr[:-1] if x <= pivot]  # elements smaller than pivot
    R = [x for x in arr[:-1] if x > pivot]   # elements larger than pivot

    L = quick_sort(L)        # recursively sort left
    R = quick_sort(R)        # recursively sort right

    return L + [pivot] + R   # combine in sorted order

def answer(arr, n):
    descending_order = quick_sort(arr)       # sort in ascending order
    descending_order = descending_order[::-1]  # reverse to get descending
    return descending_order[n-1]             # return kth largest (0-indexed)

nums = [3, 2, 1, 5, 4, 7, 6]
(answer(nums, 6))

"""5) Given an array of strings, sort them by their length using insertion sort."""

def insertion_sort_strings(arr):
    n = len(arr)
    for i in range(1, n):           # start from index 1, treat left as sorted
        for j in range(i, 0, -1):   # move left from current position
            if len(arr[j-1]) > len(arr[j]):      # compare string lengths
                arr[j-1], arr[j] = arr[j], arr[j-1]  # swap if out of order
            else:
                break               # already in correct position, stop early
    return arr

e = ["banana", "apple", "fig", "kiwi", "strawberry"]
(insertion_sort_strings(e))

"""6) Given an array of integers, sort it using selection sort and return the index of each element as it gets placed in its correct position."""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):               # i marks the boundary of sorted portion
        min_index = i                # assume current position has minimum
        for j in range(i+1, n):      # scan unsorted portion
            if arr[j] < arr[min_index]:  # found smaller element
                min_index = j            # update minimum index
        arr[i], arr[min_index] = arr[min_index], arr[i]  # place minimum at position i

    for i in range(n):
        print("Index", i, ":", arr[i])   # print each element with its final index

nums = [64, 25, 12, 22, 11]
selection_sort(nums)     