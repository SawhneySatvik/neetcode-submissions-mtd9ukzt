class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        key = ''.join(sorted(s1))
        l, r = 0, len(s1)-1

        for i in range(r, len(s2)):
            print(s2[l:r+1])
            if ''.join(sorted(s2[l:r+1])) == key:
                return True
            l += 1
            r += 1
        
        return False
