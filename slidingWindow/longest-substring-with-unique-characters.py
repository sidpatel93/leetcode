
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


print(lengthOfLongestSubstring("abcabcbb"))

print(lengthOfLongestSubstring("bbbb"))

print(lengthOfLongestSubstring("aab"))