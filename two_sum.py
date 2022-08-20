from typing import List


def find_sum(lst: List[int], k: int) -> List[int]:
  # Write your code here
  nums = {}
  for ind, num in enumerate(lst):
    if(k-num in nums):
      return [nums[k-num], ind]
    nums[num] = ind
  return None


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))