
# Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

import pytest

def thirdMax(nums):
    temp = set(nums)
    nums = list(temp) 
    nums.sort(reverse = True)
    # test = []
    if(len(nums) < 3):
        return nums[0]
    cur = 2
    pre = 1
    for i,j in enumerate(nums):
        if(nums[cur] == nums[pre]):
            pre = cur
            cur+=1
            continue
        return nums[cur]

            
print(thirdMax([2,2,3,1]));



# Test Cases

testCases= [
  ([3,2,1],1),
  ([1,2], 2),
  ([2,2,3,1], 1),
  ([1,1,2], 2)
]

def test_thirdMax():
  for test,expect in testCases:
    assert(thirdMax(test) == expect)