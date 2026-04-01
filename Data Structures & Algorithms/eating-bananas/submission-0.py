import math
class Solution:
    def hoursTaken(self, piles:List[int], speed:int) -> int:
        hours = 0
        for pile in piles:
            hours += (math.ceil(pile/speed))
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        ans = 0
        low, high = 1, max_speed

        while low <= high:
            mid = (low+high)//2
            
            if self.hoursTaken(piles, mid) <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans