class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        if len(grid)%2!=0:
            n=len(grid)//2
            left=0
            right=-1
            for i in range(n):
                if grid[i][left]!=0 and grid[i][right]!=0:
                    left+=1
                    right-=1
                else:
                    return False
            #left-=1
            #right+=1
            for i in range(n,len(grid)):
                #print(i,left,right)
                if grid[i][left]!=0 and grid[i][right]!=0:
                    left-=1
                    right+=1
                else:
                    #print(i)
                    return False
        else:
            n=len(grid)//2
            left=0
            right=-1
            for i in range(n):
                if grid[i][left]!=0 and grid[i][right]!=0:
                    left+=1
                    right-=1
                else:
                    return False
            left-=1
            right+=1
            for i in range(n,len(grid)):
                #print(i,left,right)
                if grid[i][left]!=0 and grid[i][right]!=0:
                    left-=1
                    right+=1
                else:
                    #print(i)
                    return False
        if len(grid)%2==0:
            total=len(grid)*2
        else:
            total=(len(grid)*2) -1

        count = 0
        for i in grid:
            count+=i.count(0)
        print(len(grid)**2,count,total)
        if (len(grid)**2)-count==total:
            return True
        else:
            return False