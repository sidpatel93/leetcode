from typing import List


def findmax(nums):
    window = 0
    consi = 0
    for i in range(0, len(nums)):

        if (nums[i] == 1):
            window += 1

        elif (nums[i] == 0):

            if (consi <= window):
                consi = window
                window = 0
            window = 0
    if (window >= consi):
        return window
    else:
        return consi

print(findmax([1,1,1,0,0,0,1,1]))