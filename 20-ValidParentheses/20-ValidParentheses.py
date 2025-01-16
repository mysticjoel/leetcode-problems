class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        data = {'}':'{',')':'(',']':'['}
        for i in s:
            if i in data:
                #print(stack)
                if stack and stack[-1]==data[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False