class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                #this helps in rounding up or we can import math and use the .ceil method - hours += math.ceil(pile / mid)
                hours += (pile + mid - 1) // mid

            if hours > h:
                left = mid + 1
            else:
                right = mid - 1

        return left