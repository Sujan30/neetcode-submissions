class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_map( n: str):
            """
            Given a string, we will return a dictionary
            """
            dictionary = {}
            for ch in n:
                if ch not in dictionary:
                    dictionary[ch] = 1
                else:
                    dictionary[ch]+=1
            return dictionary

        if get_map(s) == get_map(t):
            return True
        return False

        
        