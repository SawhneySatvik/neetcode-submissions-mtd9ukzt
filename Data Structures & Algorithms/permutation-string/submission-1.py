class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = Counter(s1)
        l, r = 0, len(s1)-1

        seen = Counter(s2[l:r+1])
        while r < len(s2):
            if seen == s1_map:
                return True
            seen[s2[l]] -= 1
            if seen[s2[l]] == 0:
                del seen[s2[l]]
            
            l+=1
            r+=1

            if r < len(s2):
                seen[s2[r]] += 1

        
        return False
