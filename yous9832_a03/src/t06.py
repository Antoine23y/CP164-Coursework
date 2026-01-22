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
from functions import postfix

test_expressions = [
    "12 5 -",
    "4 5 + 12 * 2 3 * -",
    "7 2 + 3 /"
]

for expr in test_expressions:
    result = postfix(expr)
    print(f"'{expr}' evaluates to {result}")
