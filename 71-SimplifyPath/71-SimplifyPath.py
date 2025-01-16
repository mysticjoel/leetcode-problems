class Solution:
    def simplifyPath(self, path: str) -> str:
        new = path.split("/")
        print(new)
        stack = []
        for i in new:
            if i=='':
                #stack.append('/')
                continue
            elif i=='.':
                continue
            elif i=='..':
                if len(stack)>0:
                    stack.pop()
                    #stack.pop()
            else:
                stack.append(i)
            print(stack)
        #if len(stack)>1:
            #stack.pop()
        return "/"+"/".join(stack)