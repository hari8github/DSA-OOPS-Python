def sum(numbers):
    """
    so here we shrink the list from 1st index and make the list to 1 element and 
    add this one with the next one till the list is completed and 
    then finally add the 1st element (0th index) and then we terminate the function
    """
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return remaining_sum + numbers[0]

numbers = [1,2,3,4,5]

print(sum(numbers))

