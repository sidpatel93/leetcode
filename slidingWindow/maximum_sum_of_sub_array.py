# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  if(k > len(arr)):
    return -1
  result = sum(arr[0:k])
  preWindow = sum(arr[0:k])
  for windowStart in range(1, len(arr)-k+1):
    newWindow = preWindow + arr[windowStart + (k - 1)] - arr[windowStart - 1]
    preWindow = newWindow
    result = max(result, newWindow)
  return result
      
print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
