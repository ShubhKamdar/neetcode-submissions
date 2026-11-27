class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        maxArea = 0

        while left < right:
            if heights[left] >= heights[right]:
                area = (heights[right] * (right - left))
                maxArea = max(maxArea,area)
                right -=1
            else:
                area = (heights[left] * (right - left))
                maxArea = max(maxArea,area)
                left +=1
        return maxArea