class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        for x in strs:
            y = frozenset(Counter(x).items())
            if y in d:
                d[y].append(x)
            else:
                d[y] = [x]
                
        return list(d.values())