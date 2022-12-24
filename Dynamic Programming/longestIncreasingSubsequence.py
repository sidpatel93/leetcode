def longestSubsequence(nums):
  lengths = [0 for i in range(len(nums))]
  for i in range(len(nums)):
    lengths[i] = 1
    for j in range(0,i):
      if nums[j] < nums[i] and lengths[i] < 1 + lengths[j]:
        lengths[i] = 1 + lengths[j]
  max_index = 0
  for i in range(1,len(lengths)):
    if lengths[i] > lengths[max_index]:
      max_index = i
  return lengths[max_index]

print(longestSubsequence([5,7,4,-3,9,1,10,4,5,8,9,3]))
print(longestSubsequence([10,9,2,5,3,7,101,18]))

