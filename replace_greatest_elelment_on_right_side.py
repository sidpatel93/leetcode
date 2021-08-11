import pytest

def myfunc(nums):    
    
    #intial max = -1
    initialMax = -1;
    
    #loop the array in reverse order
    for i in range(len(nums)-1, -1, -1):
        #new Max = max(oldmax, a[i])
        newMax = max(initialMax, nums[i])
        nums[i] = initialMax
        initialMax = newMax
    return nums



testCases= [
    ([17,18,5,4,6,1], [18,6,6,6,1,-1])
]

def test_myfunc():
    for test,expected in testCases:
        assert(myfunc(test) == expected)