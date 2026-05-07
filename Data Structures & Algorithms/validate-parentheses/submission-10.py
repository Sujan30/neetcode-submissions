class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        
        for p in s:
            if p in dic.values():
                stack.append(p)
            elif len(stack) != 0 and stack[-1] == dic[p]:
                    stack.pop()
            else:
                return False
        return len(stack) == 0