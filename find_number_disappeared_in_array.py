

def findDisappearedNumbers(nums):
    arrayToReturn = []
    compare = [0] * len(nums)
    for i in nums:
        compare[i-1] = 1
    for j in range(len(compare)):
        if (compare[j] == 0):
            arrayToReturn.append(j+1)
    return arrayToReturn

print(findDisappearedNumbers([1,2,4,1,4,2]))



test_cases = [
    ([4,3,2,7,8,2,3,1], [5,6]),
    ([1,1], [2])
]

def test_findDisappearedNumbers():
    for test, expected in test_cases:
        assert (findDisappearedNumbers(test) == expected)
    