class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        new = []
        size = len(code)
        if k>0:
            for i in range(size):
                sums = 0
                if i+k>=size:
                    sums += (sum(code[i+1:size])  + sum(code[0:((i+k)%size)+1]))
                    new.append(sums)
                else:
                    sums += sum(code[i+1:i+k+1])
                    new.append(sums)

        else:
            vnew = [0]*len(code)
            for i in range(size-1,-1,-1):
                sums = 0
                if i+k<=0:
                    #print(i,(-k-i)%size)
                    #print(code[0:i],sum(code[0:i]),sum(code[size-1:size-1-((-k-i)%size):-1]),code[size-1:size-1-((-k-i)%size):-1])
                    sums+= (sum(code[0:i])+ sum(code[size-1:size-1-((-k-i)%size):-1]))
                    vnew[i]=sums
                else:
                    #print(code[i-1:i+k-1:-1],sum(code[i-1:i+k-1:-1]))
                    sums += sum(code[i-1:i+k-1:-1])
                    vnew[i]=sums

            return vnew
        return new