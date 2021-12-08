
def lengthOfLongestSubstring(s):
    windowStart = 0
    longestString = 0
    charCount = {}
    for windowEnd in range(len(s)):
        if(s[windowEnd] in charCount and charCount[s[windowEnd]] >= windowStart):
            windowStart = charCount[s[windowEnd]] + 1
        longestString = max(longestString, windowEnd - windowStart +1)
        charCount[s[windowEnd]] = windowEnd
    return longestString

def anotherLengthOfLongestSubstring(s):
    start = 0
    end = 0
    maxLength = 0
    charSet = set()
    while(end < len(s)):
        if s[end] not in charSet:
            charSet.add(s[end])
            end += 1
            maxLength = max(maxLength, len(charSet))
        else:
            charSet.remove(s[start])
            start += 1
    return maxLength


print(anotherLengthOfLongestSubstring("abcabcbb"))

print(anotherLengthOfLongestSubstring("bbbb"))

print(anotherLengthOfLongestSubstring("aab"))