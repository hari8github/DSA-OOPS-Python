"""1) Given an array and integer k, find the maximum sum of any subarray of size k."""
def max_sum(arr, k):
    window_sum = sum(arr[:k])    # sum of first window of size k
    max_add = 0

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]   # slide: add new element, remove oldest
        max_add = max(max_add, window_sum) # update max if current window is larger

    return max_add

nums = [1,2,3,4,5,6,7,8,9]
(max_sum(nums, 3))

"""2) Given a string, find the longest substring with at most 2 distinct characters."""
def longest_substring_2(str):
    dict = {}
    l = 0
    max_len = 0
    
    for r in range(len(str)):
        dict[str[r]] = dict.get(str[r], 0) + 1

        while len(dict)>2:
            dict[str[l]] -= 1
            if dict[str[l]] == 0:
                del dict[str[l]]

            l += 1
        max_len = max(max_len, r-l+1)
    return max_len

(longest_substring_2("adadadadadadadadadadadadadabccb"))

"""3) Given an array of integers and target sum, find the minimum length subarray whose sum is greater than or equal to target."""
def find_sum_min_length(arr, target):
    l = 0
    summ = 0
    min_len = float('inf')

    for r in range(len(arr)):
        summ += arr[r]
        while summ >= target:
            min_len = min(min_len, r-l+1)
            summ -= arr[l]
            l +=1

    return min_len if min_len != float('inf') else 0
nums = [1,2,3]
(find_sum_min_length(nums, 4))

"""4) Given a string s and a pattern p, find all starting indices of p's anagrams in s."""
def strings_patterns(s, p):
    sCount, pCount = {}, {}
    for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

    res = [0] if sCount == pCount else []
    l = 0

    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
        sCount[s[l]] -= 1

        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        l += 1
        if sCount == pCount:
            res.append(l)

    return res

(strings_patterns("cbaebabacd", "abc"))

"""5) Given a string, find the longest substring with at most k distinct characters."""