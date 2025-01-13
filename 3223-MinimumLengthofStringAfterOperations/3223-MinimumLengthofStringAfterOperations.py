class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        print(d)
        count = 0
        for i,val in d.items():
            if val<=2:
                count+=val
            else:
                if val%2==0:
                    count+=2
                else:
                    count+=1
            #print(val)
        return count

