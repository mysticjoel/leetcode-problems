import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+','-','*','/']
        stack = []
        for i in tokens:
            if i not in op:
                stack.append(i)
            else:
                leftmost = int(stack.pop())
                rightmost = int(stack.pop())
                #print(leftmost,i,rightmost)
                if i=='+':
                    result = rightmost + leftmost
                elif i=='-':
                    result = rightmost - leftmost
                elif i=='*':
                    result = rightmost * leftmost
                elif i=='/':
                    result = int(rightmost / leftmost)
                stack.append(result)
                #print(stack)
        
        return int(stack[0])