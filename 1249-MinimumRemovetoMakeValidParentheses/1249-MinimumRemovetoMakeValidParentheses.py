# Last updated: 9/15/2025, 12:40:21 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        li = list(s)
        stack = []
        indexes_to_remove = set()
        for i, char in enumerate(li):
            if char=='(':
                stack.append(i)
            elif char==')':
                if not stack:
                    indexes_to_remove.add(i)
                else:
                    stack.pop()
        indexes_to_remove.update(stack)
        result = [char for i, char in enumerate(li) if i not in indexes_to_remove]
        return "".join(result)