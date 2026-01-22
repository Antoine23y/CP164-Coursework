"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antoine Youssef
ID:      169069832
Email:   yous9832@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""

from functions import is_palindrome

test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "No 'x' in Nixon"]

for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' is a palindrome: {result}")
