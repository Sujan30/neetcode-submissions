class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            words[sorted_word].append(s)
        return list(words.values())
        