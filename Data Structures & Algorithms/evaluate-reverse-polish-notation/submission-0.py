class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        mappings = {
            '+' : lambda a,b : int(a+b),
            '-' : lambda a,b : int(a-b),
            '*' : lambda a,b : int(a*b),
            '/' : lambda a,b : int(a/b)
        }        

        for s in tokens:
            if s == '+' or s == '-' or s == '*' or s =='/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(mappings[s](num2, num1))
            else:
                stack.append(int(s))
        return stack[-1]