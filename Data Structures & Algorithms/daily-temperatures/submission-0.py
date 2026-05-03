class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        for i in range(len(temperatures)):
            x = 0
            for j in range(i+1, len(temperatures)):
                
                if temperatures[j] > temperatures[i]:
                    x = j-i
                    break
                else:
                    x = 0
            results.append(x)
                
        return results
