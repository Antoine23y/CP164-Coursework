"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
from List_linked import List

my_list = List()

my_list.append(2)
my_list.append(22)
my_list.append(33)
my_list.append(11)
my_list.append(55)
my_list.append(44)

print(my_list.__setitem__(3, 99))
