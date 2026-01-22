"""
-------------------------------------------------------
Assignment 8, Task 2
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total

# Constants
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()
bst2 = BST()
bst3 = BST()

for letter in DATA1:
    bst.insert(Letter(letter.upper()))

for letter in DATA2:
    bst2.insert(Letter(letter.upper()))

for letter in DATA3:
    bst3.insert(Letter(letter.upper()))


fh = open('miserables.txt', 'r')
do_comparisons(fh, bst)
t1 = comparison_total(bst)

fh = open('miserables.txt', 'r')
do_comparisons(fh, bst2)
t2 = comparison_total(bst2)

fh = open('miserables.txt', 'r')
do_comparisons(fh, bst3)
t3 = comparison_total(bst3)

print(f"DATA1 Testing Length: {t1}")
print(f"DATA2 Testing Length: {t2}")
print(f"DATA3 Testing Length: {t3}")
