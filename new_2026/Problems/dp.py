"""Given n stairs, you can climb 1 or 2 steps at a time. Find the number of ways to reach the top."""
from functools import cache


def stairs_naive(n):
    if n <= 1:
        return n
    return stairs_naive(n-1) + stairs_naive(n-2)

(stairs_naive(7))

def stairs_top_down(n):
    memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = stairs_top_down(n-1) + stairs_top_down(n-2)
    return memo[n]

(stairs_top_down(7))

def stairs_bottom_up(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

(stairs_bottom_up(8))

def stairs_bottom_up_constant(n):
    a,b = 0,1
    for _ in range(2, n+1):
        a,b = b , a+b
    return b

(stairs_bottom_up_constant(10))

"""2) Given an array of integers, find the length of the longest increasing subsequence."""
def longest_subsequence(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i]> nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]
(longest_subsequence(nums))

"""3) Given a string, find the length of the longest palindromic subsequence."""
def palindrome_subsequence(str):
    str2 = str[::-1]
    m , n = len(str), len(str2)
    memo = {}

    def longest(x, y):
        if x == m or y == n:
            return 0
        if (x, y) in memo:
            return memo[(x, y)]
        if str[x] == str2[y]:
            result  = 1 + longest(x+1, y+1)
        else:
            result = max(longest(x+1, y), longest(x, y+1))
        memo[(x, y)] = result
        return result

    return longest(0,0)
str = "ccbc"
(palindrome_subsequence(str))

"""4) Given two strings, find the length of the longest common subsequence."""
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    memo = {}
    def longest(i, j):
        if i == m or j == n:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if str1[i] == str2[j]:
            result = 1 + longest(i+1, j+1)
        else:
            result = max(longest(i+1, j), longest(i, j+1))
        memo[(i, j)] = result
        return result
    return longest(0, 0)

text1 = 'abceeee'
text2 = 'allllblclllleee'
(lcs(text1, text2))

"""5) Given a list of items with weights and values, and a knapsack with capacity W, find the maximum value you can carry."""

def knapsack(weight, values, W):
    n = len(weight)
    memo = {}

    def solve(i, w):
        if i == n or w == 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]
        if weight[i] > w:
            result = 1 + solve(i+1, w)
        else:
            skip = solve(i+1, w)
            take = values[i] + solve(i+1, w - weight[i])
            result = max(skip, take)

        memo[(i, w)] = result
        return result

    return solve(0, W)

weight = [1,3,4,5]
values = [1,4,5,7]
W = 8
print(knapsack(weight, values, W))