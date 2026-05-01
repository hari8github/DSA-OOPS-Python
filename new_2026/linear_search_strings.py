names = ["Fernando Sucre", "Erin Hannon", "Abed? No", "T-Bag", "Pam Beesly", "Brooke", "Kevin Malone", "Jim Halpert", "Lydia Rodarte-Quayle", "Phyllis Vance", "Darryl Philbin", "Betsy Kettleman", "Ted Mosby", "Jesse Pinkman", "Karen Filippelli", "Pete Miller", "Marshall Eriksen", "Susan Ross", "Rita", "Walter White", "Gretchen Schwartz", "Ryan Howard", "Nellie Bertram", "Brian Zarycki", "Mikayla? No", "Angela Martin", "Bob Vance", "Ben Linus? No", "Creed Bratton", "Stella Zinman", "Holly Flax", "Gus Fring", "Sara Tancredi", "Lynette? No", "Toby Flenderson", "Jan Levinson", "Fernando", "Barney Stinson", "Lorelai? No", "Mose Schrute", "Michael Scofield", "Meredith Palmer", "Lily Aldrin", "Saul Goodman", "Skyler White", "Hank Schrader", "Robin Scherbatsky", "Michael Scott", "Dwight Schrute", "Oscar Martinez"]

def index_of_item(collections, target):
    for i in range(len(collections)):
        if target == collections[i]:
            return i
    return None

def load_names_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

file_names = load_names_from_file("unsorted.txt")

count = 0
for n in file_names:
    index = index_of_item(names, n)   # search in the hardcoded list
    if index is not None:
        print(index)
        count += 1
print("count: ", count)