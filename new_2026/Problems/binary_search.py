"""1) Given a sorted array and a target, return the index of the target using binary search. Return -1 if not found."""

def binary_index(arr, target):
    N = len(arr)
    L = 0
    R = N - 1                        # search space is entire array

    while L <= R:                    # continue while valid search space exists
        M = L + ((R - L) // 2)       # mid index — avoids integer overflow

        if arr[M] == target:         # found target
            return M
        elif arr[M] < target:        # target is in right half
            L = M + 1
        else:                        # target is in left half
            R = M - 1

    return -1                        # target not found

nums = [10,20,30,40,50]
(binary_index(nums, 10))

"""2)  Given a sorted array, find the leftmost index of a target value (first occurrence)."""

def binary_search_condition_based(arr, target):
    N = len(arr)
    L = 0
    R = N - 1                    # search space is entire array

    while L < R:                 # stop when L and R converge
        M = (L + R) // 2

        if arr[M] >= target:     # mid is target or too large — search left half
            R = M                # don't exclude M, it could be the answer
        else:                    # mid is too small — search right half
            L = M + 1

    return L                     # L is the leftmost index of target

nums = [1,1,1,2,2,2,2,2,3]
(binary_search_condition_based(nums, 1))

"""3) Given a sorted array of 0s and 1s, find the index of the first 1."""

def binary_search_condition_based_1(arr):
    N = len(arr)
    L = 0
    R = N - 1                    # search space is entire array

    while L < R:                 # stop when L and R converge
        M = (L + R) // 2

        if arr[M] == 1:          # found a 1 — search left for earlier occurrence
            R = M
        else:                    # found 0 — first 1 must be to the right
            L = M + 1

    return L                     # L is the index of first 1

arr = [0,0,1,1,1,1,1]
(binary_search_condition_based_1(arr))

"""4) Given a number N, find its square root using binary search (return floor value)."""

def binary_search_range_based(target, L, R):
    result = 0                   # stores the floor square root candidate
    while L <= R:                # continue while valid search space exists
        M = (L + R) // 2

        if M * M <= target:      # M is a valid floor candidate
            result = M           # save it and search right for a larger valid M
            L = M + 1
        else:                    # M is too large — search left
            R = M - 1

    return result                # largest M where M * M <= target

(binary_search_range_based(123,1,200))

"""5) Given a sorted array rotated at some pivot, find a target value."""