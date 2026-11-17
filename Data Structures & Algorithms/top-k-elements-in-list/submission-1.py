class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            maps[num] = maps.get(num, 0) + 1
        sorts = sorted(maps, key = maps.get, reverse = True)
        # we are sorting the keys of the dictionary based on its values and then returning the top
        return sorts[:k]