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
from Sorts_List_linked import Sorts
from List_linked import List

lst = List()

lst.append(9999)
lst.append(1231231231)
lst.append(341)
lst.append(44120)
lst.append(11239)
lst.append(23)

Sorts.radix_sort(lst)

for i in lst:
    print(i)
