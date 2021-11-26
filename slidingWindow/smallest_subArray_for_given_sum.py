# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
# or [1, 1, 6].

import math

def smallest_subarray_with_given_sum(s, arr):
  minLen = math.inf
  windowStart = 0
  windowSum = 0

  for windowEnd in range(0,len(arr)):
    windowSum += arr[windowEnd]
    while windowSum >= s:
      minLen = min(minLen, windowEnd - windowStart + 1)
      windowSum -= arr[windowStart]
      windowStart += 1
  if minLen == math.inf:
    return -1
  return minLen


print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))