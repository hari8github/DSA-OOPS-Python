"""1) Given a string containing ()[]{}, return True if the brackets are balanced, False otherwise."""

def bracket_check(str):
    matching = {')': '(', ']': '[', '}': '{'}  # closing bracket maps to its opening pair
    stk = []

    for i in str:
        if i not in matching:        # opening bracket — push to stack
            stk.append(i)
        else:                        # closing bracket — check against stack
            if not stk:              # stack empty, no matching opener — invalid
                return False
            else:
                popped = stk.pop()           # remove top of stack
                if popped != matching[i]:    # top doesn't match expected opener — invalid
                    return False
    return not stk                   # True if stack empty (all matched), False otherwise

str = "[{}]"
(bracket_check(str))

"""2) Given a stack, reverse its contents without using any other data structure except another stack."""

def reverse_stk(stk1):
    stk2 = []                    # second stack to hold reversed elements
    for _ in range(len(stk1)):
        x = stk1.pop()           # pop from top of original stack
        stk2.append(x)           # push to second stack — reverses order
    return stk2                  # stk2 is now reversed

stk1 = [1,2,3,4,5]
(reverse_stk(stk1))

"""3) Implement a queue using two stacks."""

class QueueusingStacks:
    def __init__(self):
        self.s1 = []    # stack for enqueue operations
        self.s2 = []    # stack for dequeue operations

    def enqueue_stk(self, x):
        self.s1.append(x)       # push new element onto s1

    def dequeue_stk(self):
        if not self.s2:          # s2 empty — transfer all elements from s1
            while self.s1:
                self.s2.append(self.s1.pop())  # reverse order into s2
        return self.s2.pop()     # pop from s2 gives oldest element (FIFO)

q = QueueusingStacks()
q.enqueue_stk(1)
q.enqueue_stk(2)
q.enqueue_stk(3)
(q.dequeue_stk())
(q.dequeue_stk())

"""4) Given a queue, reverse its contents using a stack."""
from collections import deque

def reverse_queue(arr):
    stk = []
    for _ in range(len(arr)):
        popped = arr.popleft()   # dequeue from front of queue
        stk.append(popped)       # push onto stack — reverses order
    for _ in range(len(stk)):
        back_pop = stk.pop()     # pop from stack (LIFO)
        arr.append(back_pop)     # enqueue back to queue — now reversed
    return arr

nums = deque([1,2,3,4,5])
(nums)
(reverse_queue(nums))

"""5) Generate binary numbers from 1 to N using a queue."""
from collections import deque

def binary_gen(val):
    temp = deque(["1"])     # queue starting with "1"
    result = []             # stores generated binary numbers
    for _ in range(val):
        curr = temp.popleft()       # dequeue front element
        result.append(curr)         # add to result
        temp.append(curr + "0")     # enqueue current + "0" (left child)
        temp.append(curr + "1")     # enqueue current + "1" (right child)
    return result

(binary_gen(5))

"""6) Given a queue, return the maximum element without removing any elements."""

def max_q(arr):
    max_val = 0              # tracks maximum value found so far
    for i in arr:            # iterate directly over queue — no popping needed
        if i > max_val:      # found a larger value
            max_val = i      # update max
    return max_val           # return maximum element

nums = deque([-1, -2, -3])
(max_q(nums))