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
from functions import stack_maze

maze = {
    'Start': ['A'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F', 'X'],
    'F': ['G'],
    'G': ['C']
}

print(maze)

# Expected output: ['A', 'C', 'E', 'X']
print(stack_maze(maze))
