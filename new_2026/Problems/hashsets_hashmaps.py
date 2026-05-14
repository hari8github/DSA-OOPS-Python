"""1) Given an array, return True if it contains any duplicates, else False."""

def check_duplicates(nums):
    s = set()                 # empty set to track unique elements
    for i in range(len(nums)):
        s.add(nums[i])             # add each element — duplicates are ignored by set
    if len(nums) == len(s):        # if lengths match, no duplicates were ignored
        return False
    return True                    # lengths differ, duplicates exist
    
nums = [1,2,3,4,54,3,2]
(check_duplicates(nums))      

"""2) Given two arrays, return the common elements between them (intersection) - without using intersection()"""

def intersection_sets(arr1, arr2):
    set1 = set()
    set2 = set()
    new_set = set()
    for i in range(len(arr1)):
        set1.add(arr1[i])        # add arr1 elements to set3
    for i in range(len(arr2)):
        set2.add(arr2[i])        # add arr2 elements to set4
                            
    for val in set1:
        if val in set2:          # O(1) lookup — check if element exists in set4
            new_set.add(val)     # common element found, add to result
    return new_set

nums1 = [6,7,8,9,1]
nums2 = [1,2,4,8,5]

(intersection_sets(nums1, nums2))

"""3) Given a string, return the character that appears the most times."""

def char_count(str):
    dictt = {}
    for i in range(len(str)):
        if str[i] in dictt:          # character already seen
            dictt[str[i]] += 1       # increment its count
        else:
            dictt[str[i]] = 1       # first occurrence, set count to 1
             
    return max(dictt, key=dictt.get) # return character with highest count

str = 'bcccccd'
(char_count(str))

"""4) Given an array of integers, return the two numbers that add up to a target. (You solved this before with O(n²) — now do it in O(1) lookup using a hashmap)"""

def hashmap_target(nums, target):
    dictt = {}                          # stores seen numbers and their indices
    for i in range(len(nums)):
        if target - nums[i] in dictt:   # check if complement exists in dict — O(1) lookup
            return nums[i], target - nums[i]  # pair found, return both numbers
        dictt[nums[i]] = i          # not found yet, store current number
    
nums = [1,2,3,4,5]
(hashmap_target(nums, 9))

"""5) Given a string, find the first non-repeating character and return its index. (You solved this before with count() — now do it with a hashmap in O(n))"""

def char_count(str):
    str_dict = {}

    for i in range(len(str)):
        if str[i] in str_dict:       # character already seen
            str_dict[str[i]] += 1    # increment its count
        else:
            str_dict[str[i]] = 1     # first occurrence, set count to 1

    for i in range(len(str)):
        if str_dict[str[i]] == 1:    # first character with count 1 is non-repeating
            return i                 # return its index

str = 'aabbc'
print(char_count(str))