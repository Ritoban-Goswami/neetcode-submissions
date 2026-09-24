class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            k = 0

            for p in piles:
               k += math.ceil(p/m)

            if k <= h:
                res = min (res, m)
                r = m - 1
            elif k > h:
                l = m + 1
        return res