def selection_sort(values):
    sorted_list = []
    print(values, "", sorted_list)
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        print(values, "", sorted_list)
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

numbers = [2,5,2,7,4,98]
print(selection_sort(numbers))

# print(values, sorted_list) is to see how the numbers are being sorted from unsorted to sorted