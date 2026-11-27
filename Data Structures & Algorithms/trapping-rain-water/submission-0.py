class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        water = 0

        leftmax = height[left]
        rightmax = height[right]

        while left < right:
            if height[left] > height[right]:
                right -=1
                rightmax = max(rightmax, height[right])
                water += rightmax - height[right]
            else:
                left +=1
                leftmax = max(leftmax, height[left])
                water += leftmax - height[left]
        return water