class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case: check if len is equal

        if len(s) != len(t):
            return False
        
        dict1 = Counter(s)
        dict2 = Counter(t)

        if dict1 == dict2:
            return True
        return False


        