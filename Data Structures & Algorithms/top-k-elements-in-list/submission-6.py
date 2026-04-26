class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = defaultdict(int)

        for num in nums:
            key[num] +=1
        
        sorted_dict = dict(sorted(key.items(), key=lambda item:item[1], reverse=True))

        return list(sorted_dict.keys())[:k]

        