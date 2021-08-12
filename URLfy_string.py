import pytest


def urlify(string, length):
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])





print(urlify(" a b    ", 4))





test_cases = [
    ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
    ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
    (" a b    ", 4, "%20a%20b"),
    (" a b       ", 5, "%20a%20b%20")
]



def test_urlify():
    for str,len,expected in test_cases:
        assert(urlify(str,len) == expected)

