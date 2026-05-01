def quicksort(values):
    if len(values) <= 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for v in values[1:]:
        if v <= pivot:
            less_than_pivot.append(v)
        else:
            greater_than_pivot.append(v)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def load_names_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

file_names = load_names_from_file("unsorted.txt")

sorted_names = quicksort(file_names)
for n in sorted_names:
    print(n)