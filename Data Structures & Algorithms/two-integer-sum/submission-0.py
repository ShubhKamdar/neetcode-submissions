class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, value in enumerate(nums):
            
            if value in map:
                return [map[value], index]
            
            map[target - value] = index

