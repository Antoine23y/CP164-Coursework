"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack

source_stack = Stack()

source_stack._values.extend([1, 2, 3])

print(f"Stack before: {source_stack._values}")

source_stack.reverse()

print(f"Stack after: {source_stack._values}")
