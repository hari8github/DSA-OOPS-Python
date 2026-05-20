"""1) Given a number N, calculate its factorial using recursion."""

def factorial(val):
    if val <= 1:        # base case — factorial of 0 or 1 is 1
        return 1
    else:
        return val * factorial(val - 1)  # multiply current val with factorial of val-1

(factorial(0))

"""2)Given a number N, return the Nth Fibonacci number using recursion."""

def fib(n):
    if n <= 1:              # base case — fib(0)=0, fib(1)=1
        return n
    else:
        return fib(n-1) + fib(n-2)  # sum of previous two fibonacci numbers

(fib(6))

"""3)Given an array, find the sum of all elements using recursion."""

def sum_of_all(arr):
    if len(arr) == 0:               # base case — empty array, return 0
        return 0
    return arr[0] + sum_of_all(arr[1:])  # first element + sum of remaining elements

arr = [10,20,30,40,50,60]
(sum_of_all(arr))

"""4) Given a string, check if it is a palindrome using recursion."""

def palindrome_check(str):
    if len(str) <= 1:               # base case — empty or single char is palindrome
        return True
    if str[0] == str[-1]:           # first and last characters match
        return palindrome_check(str[1:-1])  # recurse on middle substring
    else:
        return False                # mismatch found — not a palindrome

str = "racecar"
(palindrome_check(str))

"""5) Given a number N, calculate the sum of digits using recursion."""

def digit_sum(val):
    if val == 0:                        # base case — no digits left
        return 0
    else:
        x = val % 10                    # extract last digit
        return x + digit_sum(val // 10) # add last digit to sum of remaining digits
(digit_sum(12345))