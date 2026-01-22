"""
-------------------------------------------------------
Lab 7, Task 3 Testing
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""

from List_linked import List

my_list = List()

my_list.append(11)
my_list.append(22)
my_list.append(33)
my_list.append(44)

even, odd = my_list.split_alt()

for x in even:

    print(x)
