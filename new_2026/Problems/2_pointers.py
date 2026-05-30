"""1) Given a sorted array and a target, find two numbers that add up to the target. Return their indices."""

from tabnanny import check


def sum_target(arr, target):
    left = 0
    right = len(arr) - 1       # start pointers at both ends
    while left <= right:
        if arr[left] + arr[right] == target:   # found the pair
            return left, right
        elif arr[left] + arr[right] < target:  # sum too small — move left right
            left += 1
        else:                                   # sum too large — move right left
            right -= 1

nums = [2,2,22,24]
(sum_target(nums, 4))

"""2) Given a string, check if it is a palindrome ignoring non-alphanumeric characters using two pointers."""

def check_palindrome(str):
    str = ''.join(c.lower() for c in str if c.isalnum())  # remove non-alphanumeric and lowercase
    left = 0
    right = len(str) - 1          # pointers at both ends
    while left <= right:
        if str[left] != str[right]:   # mismatch found — not palindrome
            return False
        left += 1                     # move inward
        right -= 1
    return True                       # all characters matched               # all characters matched

(check_palindrome("mal  am"))

"""3) Given a sorted array, remove duplicates in-place using two pointers and return the new length."""

def rem_dupli(arr):
    l = 0                          # tracks last unique element position
    for r in range(l, len(arr)):   # r scans entire array
        if arr[r] != arr[l]:       # found new unique element
            l += 1                 # move l forward to claim next slot
            arr[l] = arr[r]        # overwrite with new unique value
    print("New array: ", arr[:l+1], "and its length is: ", l+1)  # slice to get unique portion

nums = [1,1,2,2,3,4,5,6,6,7,7,8]
#rem_dupli(nums)

"""4) Given an array of integers, find the container that holds the most water. """
def water_container(arr):
    n = len(arr)
    l = 0
    r = n - 1                        # pointers at both ends
    max_area = 0

    while l < r:
        w = r - l                    # width between the two lines
        h = min(arr[l], arr[r])      # height limited by shorter line
        a = w * h                    # area of container
        max_area = max(max_area, a)  # update max if larger

        if arr[l] < arr[r]:          # move the shorter line inward
            l += 1
        else:
            r -= 1

    return max_area

nums = [1, 8, 6, 2, 5, 4, 100, 3, 7]
(water_container(nums))

"""5) Given an array, find three numbers that add up to zero. Return all unique triplets."""

def three_sum(nums):
    nums.sort()                          # sort to enable two pointers and duplicate skipping
    n = len(nums)
    answer = []

    for i in range(n):
        if nums[i] > 0:                  # sorted — if first num positive, sum can't be 0
            break
        elif i > 0 and nums[i] == nums[i-1]:  # skip duplicate first numbers
            continue

        lo, hi = i+1, n-1               # two pointers for remaining elements
        while lo < hi:
            summ = nums[i] + nums[lo] + nums[hi]
            if summ == 0:                # found valid triplet
                answer.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo+1, hi-1     # move both pointers inward

                while lo < hi and nums[lo] == nums[lo-1]:   # skip duplicate lo values
                    lo += 1
                while lo < hi and nums[hi] == nums[hi+1]:   # skip duplicate hi values
                    hi -= 1
            elif summ < 0:              # sum too small — move lo right
                lo += 1
            else:                       # sum too large — move hi left
                hi -= 1

    return answer

nums = [-4, -1, -1, 0, 1, 2, -3]
(three_sum(nums))