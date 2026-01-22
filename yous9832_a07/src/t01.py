"""
-------------------------------------------------------
Lab 6, Task 1 Testing
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-03-10"
-------------------------------------------------------
"""

from List_linked import List

my_list = List()

my_list.append(22)
my_list.append(33)
my_list.append(11)
my_list.append(55)
my_list.append(44)

my_list.insert(2, 0)

loop = my_list._front

while loop != None:

    print(loop._value)

    loop = loop._next
