class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq, max_count = 0, 0
        seen = defaultdict(int)
        l, r = 0, 0

        while l<=r and r<len(s):
            seen[s[r]] += 1
            max_freq = max(max_freq, seen[s[r]])
            while (r-l+1)-max_freq > k:
                seen[s[l]] -= 1
                l += 1
            max_count = max(max_count, (r-l+1))
            r += 1
        
        return max_count