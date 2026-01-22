"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_rear(123)
a.insert_rear(1)
a.insert_rear(213441)
a.insert_rear(14)
a.insert_rear(12351235)
a.insert_rear(1213213123)
a.insert_rear(0)
a.insert_rear(-1)

Sorts.gnome_sort(a)

for i in a:
    print(i)
