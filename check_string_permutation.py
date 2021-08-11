import pytest

def myfunc(str1,str2):
    if len(str1)!=len(str2):
        return False
    list1 = list(str1)
    list2 = list(str2)
    if(sorted(list1) == sorted(list2)):
        return True
    return False


print(myfunc("abcd", "d2cba"))


test_cases = (
    ("dog", "god", True),
    ("abcd", "bacd", True),
    ("3563476", "7334566", True),
    ("wef34f", "wffe34", True),
    ("dogx", "godz", False),
    ("abcd", "d2cba", False),
    ("2354", "1234", False),
    ("dcw4f", "dcw5f", False),
    ("DOG", "dog", False),
    ("dog ", "dog", False),
    ("aaab", "bbba", False),
)

def test_myfunc():
    for str1,str2,expected in test_cases:
        assert(myfunc(str1,str2) == expected)