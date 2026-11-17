class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #The first solution I could think of 
        maps = {}
        for num in nums:
            maps[num] = maps.get(num,0) + 1
        
        sorts = sorted(maps, key=maps.get, reverse = True)

        return sorts[:k]