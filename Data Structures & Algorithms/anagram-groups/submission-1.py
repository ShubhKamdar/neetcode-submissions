class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}

        for words in strs:
            if tuple(sorted(words)) not in maps:
                maps[tuple(sorted(words))] = []
            
            maps[tuple(sorted(words))].append(words)
        
        return list(maps.values())