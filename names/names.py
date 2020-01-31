import time
from binary_search_tree import BinarySearchTree
'''
Nested for loops take 8.27 secs with O(n)
64 duplicates

Limits: cannot use list

input: both name list
output: duplicates only

Plan:
use binary search tree to improve runtime.
Import Binary search tree file, to have access to it in this file.
I need to pass in names_1 into the tree
Then loop through names_1 inserting into the tree
Then compare names_2 to names_1 tree to find dublicates.
Return count of dublicates.
'''

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

'''
==========NEW CODE==============
Runtime: 0.16054606437683105 seconds
'''
duplicates = []
tree = BinarySearchTree(names_1[0])  # set index to the first
for name in names_1:
    # insert names into the tree
    tree.insert(name)
for name in names_2:
    # compares names_2 to the tree to check if duplicate. if a duplicate it places it in the duplicate array.
    if tree.contains(name):
        duplicates.append(name)


# OLD CODE WITH 8.27 sec run time
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
