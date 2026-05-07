class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)

        stack = []
        l = 0
        max_k = 0
        stack.append(s[l])

        for r in range(1,len(s)):
            while l<r and s[r] in stack:
                l+=1
                stack.pop(0)
            stack.append(s[r])
            max_k = max(r-l+1, max_k)
        return max_k
        
        