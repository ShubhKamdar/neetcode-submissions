class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        
        for word in strs:
            count = [0]*26

            for char in word:
                count[ord(char) - ord('a')] +=1
                
            key = tuple(count) #We cannot use lists as keys for the dictionary
            if key not in maps:
                maps[key] = []
            
            maps[key].append(word)
        return list(maps.values())