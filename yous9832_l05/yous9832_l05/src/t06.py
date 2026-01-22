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
from functions import bag_to_set

old = [4, 5, 3, 4, 5, 2, 2, 4]

new = bag_to_set(old)

print(f"""
Old List: {old}
New List: {new}
""")
