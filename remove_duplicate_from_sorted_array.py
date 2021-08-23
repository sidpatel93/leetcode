from typing import NoReturn


def removeDuplicates(nums):
    i = 0
    j= i+1
    while j <= (len(nums)-1):
        if(nums[i] < nums[j]):
            nums[i + 1] = nums[j]
            i =i + 1
            j = j + 1
        else:
            j =j + 1
    print(nums[: i+1])
    return(i+1)


print(removeDuplicates([0,1,1,1,2,3,3,4,4]))
