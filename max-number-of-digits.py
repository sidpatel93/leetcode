# Given an array nums of integers, return how many of them contain an even number of digits.
 

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.


# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

from typing import List
import math


def findNumbers(nums):
    evendigits = 0
    for i in nums:
        a = int(math.log10(i)) + 1
        if(a%2 == 0):
            evendigits = evendigits + 1
        else:
            pass
    return evendigits

print(findNumbers([555,6658,78,4,11,69,663]))    # Should return 4, since there are 4 numbers with even digits(6658,78,11 and 69)
