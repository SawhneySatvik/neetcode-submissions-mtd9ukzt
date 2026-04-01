class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
            
        seen = defaultdict(int)
        t_map = Counter(t)
        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(t_map)
        l = 0

        for r in range(len(s)):
            char = s[r]
            seen[char] += 1

            if char in t_map and seen[char] == t_map[char]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                seen[s[l]] -= 1

                if s[l] in t_map and seen[s[l]] < t_map[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ''


