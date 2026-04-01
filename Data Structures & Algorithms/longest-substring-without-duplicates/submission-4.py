class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        i = 0
        for j in range(len(s)):
            if s[j] in seen:
                while s[j] in seen:
                    del seen[s[i]]
                    i += 1
            seen[s[j]] = j
            longest = max(longest, j-i+1)
        
        return longest