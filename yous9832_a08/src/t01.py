"""
-------------------------------------------------------
Assignment 8, Task 1
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# imports
from BST_linked import BST


bst = BST()
bst2 = BST()

# testing equals method
equals = bst == bst2
print(f'equal test == True: {equals}')

# testing insert function
bst2.insert(10)
bst2.insert(5)
bst2.insert(15)

test_list = []
for x in bst2:
    test_list.append(x)
print(f'insert test == [10, 5, 15]: {test_list}')

# testing equals
equals = bst == bst2
print(f'equal test == False: {equals}')

# testing is_balanced
b = bst2.is_balanced()
print(f'balance test == True: {b}')

# testing is_valid
b = bst2.is_valid()
print(f'is_valid test == True: {b}')

# min test
value = bst2.min()
print(f'min test == 5: {value}')

# leaf_count test
count = bst2.leaf_count()
print(f'leaf_count test == 2: {count}')

# one_child count test
bst2.insert(2)
count = bst2.one_child_count()
print(f'one_child_count test == 1: {count}')

# two_child count test
bst2.insert(4)
bst2.insert(14)
bst2.insert(20)
count = bst2.two_child_count()
print(f'two_child_count test == 2: {count}')

# inorder test
a = bst2.inorder()
print(f'inorder test == [2, 4, 5, 10, 14, 15, 20]: {a}')

# preorder test
a = bst2.preorder()
print(f'preorder test == [10, 5, 2, 4, 15, 14, 20]: {a}')

# postorder test
a = bst2.postorder()
print(f'postorder test == [4, 2, 5, 14, 20, 15, 10]: {a}')

# levelorder test
a = bst2.levelorder()
print(f'levelorder test == [10, 5, 15, 2, 14, 20, 4]: {a}')
