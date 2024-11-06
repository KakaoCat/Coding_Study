class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        hashmap = collections.defaultdict(list)

        for str in strs:
            #hashmap["".join(sorted(str))].append(str) 
            hashmap[tuple(sorted(str))].append(str)
        
        return list(hashmap.values())
 
