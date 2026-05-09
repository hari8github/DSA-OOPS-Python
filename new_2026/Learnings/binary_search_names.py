search_names = ["Fernando Sucre", "Erin Hannon", "Abed? No", "T-Bag", "Pam Beesly", "Brooke", "Kevin Malone", "Jim Halpert", "Lydia Rodarte-Quayle", "Phyllis Vance", "Darryl Philbin", "Betsy Kettleman", "Ted Mosby", "Jesse Pinkman", "Karen Filippelli", "Pete Miller", "Marshall Eriksen", "Susan Ross", "Rita", "Walter White", "Gretchen Schwartz", "Ryan Howard", "Nellie Bertram", "Brian Zarycki", "Mikayla? No", "Angela Martin", "Bob Vance", "Ben Linus? No", "Creed Bratton", "Stella Zinman", "Holly Flax", "Gus Fring", "Sara Tancredi", "Lynette? No", "Toby Flenderson", "Jan Levinson", "Fernando", "Barney Stinson", "Lorelai? No", "Mose Schrute", "Michael Scofield", "Meredith Palmer", "Lily Aldrin", "Saul Goodman", "Skyler White", "Hank Schrader", "Robin Scherbatsky", "Michael Scott", "Dwight Schrute", "Oscar Martinez"]

def load_names_from_file(filename):
    with open(filename, "r", encoding="utf-16") as file:
        return [line.strip() for line in file if line.strip()]

file_names = load_names_from_file("sorted.txt")

def binary_search(collection, target):
    first = 0
    last = len(collection)-1
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

for n in search_names: # looping in the names to be searched. present in this file  
    index = binary_search(file_names, n) # this is the collection of sorted names.
    if index is not None:
        print(index)