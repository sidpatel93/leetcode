def sortedSquares(nums):
        
  for i in range(0,(len(nums))):
      square = nums[i]*nums[i]
      nums[i] = square
  nums.sort()
  return nums


print(sortedSquares([-4,-1,0,3,10]))