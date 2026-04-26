class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if stack:
                last = stack[-1]
                if self.isPair(last, c):
                    stack.pop()
                    continue
            stack.append(c)
        return not stack

    def isPair(self, last, c):
        if last == '(' and c == ')' or last == '{' and c == '}' or last == '[' and c == ']':
            return True
        return False

        




        