class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo = 1 
        hi = max(piles)

        def hourcount(r): 
            count = 0
            for i in range(len(piles)):
                count +=  (piles[i] + r - 1) // r 
            
            return count


        while lo < hi: 
            mid = (lo + hi) // 2 
            if hourcount(mid) <= h:
                hi = mid 
            else:
                lo = mid + 1
            
        return hi
        