import pytest


def sortedSquares(nums):
    arrayToReturn = [x*x for x in nums]      
    return(sorted(arrayToReturn))


print(sortedSquares([-4,-1,0,3,10]))



testCases = [
    ([-4,-1,0,3,10], [0,1,9,16,100])
]


def test_sortedSquares():
    for test,expected in testCases:
        assert(sortedSquares(test) == expected)