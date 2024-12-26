class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        val = r*c
        if row * col != r * c:
            return mat
        new = [] 
        flat=sum(mat, [])
        for i in range(r):
            a=[]
            for j in range(c):
                a.append(0)
            new.append(a)
      #  print(new[0][0])
        ind =0
        print(r,c)
        for i in range(r):
            for j in range(c):
                #print(i,j)
                #print(new[i][j])
                print(i,j,ind)
                new[i][j]=flat[ind]
                ind+=1
        return new