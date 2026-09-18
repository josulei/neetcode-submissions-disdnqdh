class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.helper(piles, 1, max(piles), h)

    def helper(self, piles, left, right, h):
        if left >= right: 
            return left
        else: 
            mid = (left + right) // 2
            total = 0
            for i in piles:
                total += math.ceil(float(i) / mid)
            if total > h: 
                return self.helper(piles, mid+1, right, h)
            else: 
                return self.helper(piles, left, mid, h)