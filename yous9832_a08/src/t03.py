"""
-------------------------------------------------------
Assignment 8, Task 3
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports

# Constants
from BST_linked import BST
from functions import do_comparisons, comparison_total, letter_table
from Letter import Letter

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst3 = BST()

for data in DATA3:
    letter = Letter(data)
    bst3.insert(letter)

fh = open('miserables.txt', 'r')
do_comparisons(fh, bst3)

t3 = comparison_total(bst3)

print(f"DATA3 Testing Length: {t3}")

letter_table(bst3)
