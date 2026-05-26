import heapq

"""1) Given a list of numbers, find the minimum element using a heap."""

def find_min(arr):
    heapq.heapify(arr)          # convert list to min heap in-place — O(n)
    minn = heapq.heappop(arr)   # pop and return smallest element — O(log n)
    return minn

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 7]
(find_min(nums))

"""2) Given a list of numbers, return the K largest elements."""

def k_largest(arr, n):
    new_list = []
    l = len(arr)
    for i in range(l):
        arr[i] = -arr[i]
    heapq.heapify(arr)

    for i in range(n):
        popped =  -heapq.heappop(arr)
        heapq.heappush(new_list, popped)

    return new_list

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 7]
(k_largest(nums, 3))

"""3) Given a list of numbers, sort them using heap sort."""

def heap_sort(arr):
    heapq.heapify(arr)          # convert list to min heap in-place — O(n)
    l = len(arr)
    pudhu_list = [0] * l        # initialize result list with zeros

    for i in range(l):
        minn = heapq.heappop(arr)    # pop smallest element — O(log n)
        pudhu_list[i] = minn         # place in sorted order

    return pudhu_list               # returns sorted list in ascending order

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 7]
(heap_sort(nums))

"""4) Given an array, find the Kth smallest element."""

def kth_min(arr, n):
    heapq.heapify(arr)          # convert to min heap — O(n)
    for _ in range(n):
        minn = heapq.heappop(arr)   # pop minimum n times — O(log n) each
    return minn                 # last popped value is the kth smallest

nums = [8,3,7,3,8,32,1,4]

"""5) Given a list of tasks with priorities, process them in priority order using a min heap."""

def priority_queue(arr):
    heap = []
    for i , j in arr:
        heapq.heappush(heap, (i, j))
    
    while heap:
        priority, task = heapq.heappop(heap)
        print("Processing: ", {task} )

tasks = [(1, "urgent task"), (3, "normal task"), (2, "medium task"), (5, "very low task"), (4, "low task")]
#(priority_queue(tasks))