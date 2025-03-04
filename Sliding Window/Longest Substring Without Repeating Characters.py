# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
# 2 pointer, l = 0 and r in range of len(s)
# removing duplicate first with while loop and incrementing l pointer
# adding the r pointer character to the set and checking max size of the window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(r-l+1, res)
        return res





        