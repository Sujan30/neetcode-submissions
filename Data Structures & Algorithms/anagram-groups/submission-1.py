class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for word in strs:
            sorted_string = ''.join(sorted(word))
            dictionary[sorted_string].append(word)

        return list(dictionary.values())

            
                