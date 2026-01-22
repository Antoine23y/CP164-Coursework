"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""

from Queue_circular import Queue
from functions import queue_split_alt

source = Queue()
temp = Queue()

for i in range(10):
    source.insert(i)
    temp.insert(i)

print(f"source contains: ")
while not temp.is_empty():
    print(temp.remove(), end=' ')

target1, target2 = queue_split_alt(source)

assert source.is_empty(), "Source queue should be empty after split."

print("\ntarget1 contains:")
while not target1.is_empty():
    print(target1.remove(), end=' ')

print("\ntarget2 contains:")
while not target2.is_empty():
    print(target2.remove(), end=' ')
