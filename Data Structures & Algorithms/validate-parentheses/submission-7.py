class Solution:
    def isValid(self, s: str) -> bool:
        #base case length of s is odd -> atleast 1 non pair

        if len(s) % 2 != 0:
            return False
        
        stack = []

        for p in s:
            #opening bracket
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            #closing bracket
            else: 
                if len(stack) == 0:
                    return False

                if p == ']' and '[' == stack[-1]:
                    stack.pop()
                elif p == ')' and '(' in stack[-1]:
                    stack.pop()
                elif p == '}' and '{' in stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) !=0 :
            return False
        return True

        