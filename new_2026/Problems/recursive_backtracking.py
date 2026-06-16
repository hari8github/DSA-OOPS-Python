"""1) Given a set of distinct integers, return all possible subsets that have an even sum."""


def even_subsets(nums):
    n = len(nums)
    res, sol = [], []         # res = all valid subsets, sol = current subset

    def backtrack(i):
        if i == n:            # base case — reached end of array
            if sum(sol[:]) % 2 == 0:  # only add subset if sum is even
                res.append(sol[:])    # copy of sol, not reference
            return            # always return at base case

        backtrack(i+1)        # don't pick nums[i]
        sol.append(nums[i])   # pick nums[i]
        backtrack(i+1)        # recurse with nums[i] included
        sol.pop()             # backtrack — undo the pick

    backtrack(0)
    return res

nums = [0,2, 4]
(even_subsets(nums))

"""2) Given a collection of integers that might contain duplicates, return all unique subsets."""
def rem_dupli(nums):
    n = len(nums)
    res, sol = [], []         # res = all unique subsets, sol = current subset

    def backtrack(i):
        if i == n:            # base case — reached end
            res.append(sol[:])
            return

        # pick nums[i]
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()             # backtrack — undo pick

        # don't pick — skip duplicates at same level
        while i+1 < n and nums[i] == nums[i+1]:
            i += 1            # skip past duplicate values
        backtrack(i+1)

    nums.sort()               # sort first so duplicates are adjacent
    backtrack(0)
    return res

nums = [1,1,2,2]
(rem_dupli(nums))

"""3) Given a set of distinct integers, return all possible permutations."""
def permutation_nums(nums):
    n = len(nums)
    res, sol = [], []
    used = [False] * n        # tracks which elements are currently in sol

    def backtrack(i):
        if len(sol) == n:     # complete permutation found
            res.append(sol[:])
            return
        for j in range(n):
            if not used[j]:           # element not yet used
                used[j] = True        # mark as used
                sol.append(nums[j])   # pick element
                backtrack(i+1)
                sol.pop()             # backtrack — undo pick
                used[j] = False       # mark as unused again

    backtrack(0)
    return res

nums = [1,2,4]
(permutation_nums(nums))

"""4) Given a string, generate all valid combinations of parentheses for n pairs."""
def valid_parantheses(c):
    res, sol = [], []

    def backtrack(op, cl):
        if len(sol) == 2*c:          # complete combination — 2*n brackets total
            res.append(''.join(sol)) # join list to string and save
            return
        if op < c:                   # can add '(' if open count less than n
            sol.append('(')
            backtrack(op+1, cl)      # recurse with one more open
            sol.pop()                # backtrack
        if cl < op:                  # can add ')' only if unclosed opens exist
            sol.append(')')
            backtrack(op, cl+1)      # recurse with one more close
            sol.pop()                # backtrack

    backtrack(0, 0)
    return res
    
(valid_parantheses(2))