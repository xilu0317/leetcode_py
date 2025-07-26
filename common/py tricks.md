============================================================================================================
🔥 Python LeetCode Cheatsheet
============================================================================================================

🔁 LIST TRICKS
-------------
arr[-1]           # Last element
arr[::-1]         # Reverse list
arr[:k]           # First k elements
arr[k:]           # Elements from k to end
list(set(arr))    # Remove duplicates
sum(arr)          # Sum of list

📚 SORTING
----------
arr.sort()                                # In-place sort
sorted(arr, reverse=True)                # Descending sort
arr.sort(key=lambda x: x[1])             # Sort by second element (e.g. intervals)


🎯 LIST COMPREHENSIONS
----------------------
[x*x for x in range(5)]                  # Squares: [0, 1, 4, 9, 16]
[x for x in nums if x % 2 == 0]          # Filter evens


🔢 ENUMERATE & ZIP
-------------------
for i, val in enumerate(arr):           # index and value
for a, b in zip(list1, list2):          # pairwise iteration


🧠 DICT & SET TRICKS
---------------------
from collections import Counter, defaultdict

Counter(arr)                             # Frequency count
set(arr)                                 # Unique elements, fast lookup
defaultdict(list)                        # Auto-init dict with list
dict.get(key, default)                   # Safe dict access with fallback


🔄 LOOP PATTERNS
-----------------
while left < right:                      # Two pointers
for ch in reversed(s):                   # Reverse iterate
for i in range(len(arr)-1, -1, -1):      # Reverse with index


💡 SHORT-CIRCUITING
--------------------
if not arr:                              # Check if list is empty
if a and b:                              # Both are True
res = a or b                             # a if True, else b
