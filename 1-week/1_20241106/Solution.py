class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        hashmap = collections.defaultdict(list)

        for str in strs:
            #hashmap["".join(sorted(str))].append(str) 
            hashmap[tuple(sorted(str))].append(str)
        
        return list(hashmap.values())
 
'''


        hashmap = collections.defaultdict(list)

        for str in strs: 
            new_str = [0] * 26 ## string char has assigned encoding index.
            for s in str:
                new_str[ord(s) - ord("a")] += 1 
            hashmap[tuple(new_str)].append(str)
        
        return list(hashmap.values())


'''
