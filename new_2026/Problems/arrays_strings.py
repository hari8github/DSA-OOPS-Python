"""1.  Given an array of integers, return the indices of the two numbers that add up to a target."""
def two_nums(nums, target):
    for i in range(len(nums)):        # i is the first element's index
        for j in range(i+1, len(nums)): # j starts at i+1 to avoid pairing element with itself
            if nums[i] + nums[j] == target: # check if the pair sums to target
                return [i, j]         # return indices immediately when found
    return []                         # no pair found

nums = [10, 0, 20]
(two_nums(nums, 30))

"""2.  Given an array, move all zeroes to the end while maintaining the relative order of non-zero elements"""

def move_zeroes(nums):
    for i in range(len(nums)):     # loop through each index
        if nums[i] == 0:           # if current element is zero
            nums.append(nums[i])   # add that zero to the end
            nums.remove(nums[i])   # remove the first occurrence of 0 from front             
    return nums

nums = [0, 5, 0, -1, 3, 0, 2, 8, 0, 7, -4, 6, 0, 9, 1, 0, 4, 0, 10]
(move_zeroes(nums))

"""3.  Given a sorted array, remove duplicates in-place and return the new length."""

def remove_duplicates(nums):
    l = 0                          # l tracks the last unique element's position
    for r in range(1, len(nums)):  # r scans from index 1 to end
        if nums[r] != nums[l]:     # found a new unique element
            l += 1                 # move l forward to claim next slot
            nums[l] = nums[r]      # overwrite that slot with the new unique value
    return l + 1, nums[:l+1]       # l+1 = count of unique elements, nums[:l+1] = unique array

nums = [1,1,1,1,1,1,1,2,2,3,3,4,4,5,5]
(remove_duplicates(nums))

"""3 B.  Given a sorted array, remove duplicates in-place and return the new length."""
def dupli(nums):
    new_list = []
    for i in range(len(nums)):
        if nums[i] not in new_list:
            new_list.append(nums[i])
    return len(new_list), new_list

nums = [1,1,1,1,1,1,1,2,2,3,3,4,4,5,5]
(dupli(nums))

"""4.  Given an array of integers, find the contiguous subarray with the largest sum and return that sum."""
def subarray_sum(nums):
    max_sum = 0        
    for i in range(len(nums)):       # i = start index of subarray
        current_sum = 0              # reset sum for each new starting position
        for j in range(i, len(nums)):    # j = end index, starts at i (single element subarray)
            current_sum += nums[j]   # add current element to running sum
            if current_sum > max_sum:    # check if current subarray sum is the largest so far
                max_sum = current_sum    # update max_sum if larger found
    return max_sum                   # return the largest subarray sum found

nums = [201,2,3,99,-78,99]
("Max sum is:",subarray_sum(nums))

"""5.  Given an array representing stock prices by day, find the max profit you can make by buying on one day and selling on a later day."""
def profit_calc(nums):
    buy = nums[0]              # assume we buy on the first day
    profit = 0                 # no profit initially

    for i in range(len(nums)):
        if nums[i] < buy:      # found a cheaper price to buy
            buy = nums[i]      # update buy to the new minimum
        if nums[i] - buy > profit:   # check if selling today gives better profit
            profit = nums[i] - buy   # update profit if larger
    return profit  

nums = [4,2,7,8,90,3]
(profit_calc(nums))

"""STRINGS"""

"""Given a string, check if it is a palindrome (ignore spaces, punctuation, case)."""
def palindrome(str):
    str = ''.join(c.lower() for c in str if c.isalnum())  # remove spaces/punctuation and lowercase
    if str == str[::-1]:  # compare string with its reverse
        return True
    return False

str = 'madam im adam'
(palindrome(str))

"""Given a string, find the first non-repeating character and return its index. If none, return -1."""
def str_occur(str):
    for i in range(len(str)):        # loop through each index
        if str.count(str[i]) == 1:   # check if this character appears exactly once in the string
            return i                 # return index of first non-repeating character
    return -1                        # no non-repeating character found

str = ['leetcode', 'aabb']
for i in str:
    (str_occur(i))

"""Given two strings, check if one is an anagram of the other."""
def anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = 'abdc'
str2 = 'bacd'
(anagram(str1, str2))

"""Given a sentence string, reverse the order of words. (e.g. "hello world" → "world hello")"""
def reverse_words(str):
    str = str.split()              # split string into list of words by spaces
    new_str = str[::-1]            # reverse the list of words
    new_str = ' '.join(new_str)    # join words back with space separator
    return new_str

str = 'hello bye hola'
(reverse_words(str))

"""Given a string, count the number of vowels and consonants in it."""
def substring_vc(str):
    vowels = 'a','e','i','o','u'  # tuple of vowels to check against
    count_v = 0                    # vowel counter
    count_c = 0                    # consonant counter
    for i in range(len(str)):      # loop through each character
        if str[i] in vowels:       # check if character is a vowel
            count_v += 1           # increment vowel count
        elif str[i].isalpha():     # check if character is a letter (not space/number/punctuation)
            count_c += 1           # increment consonant count (letter but not a vowel)
    return "Vowel count", count_v, "Consonant count", count_c

str = 'hello world'
(substring_vc(str))