'''import math
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        hashtable = defaultdict(int)
        for i in range(len(shifts)):
            start = shifts[i][0]
            end = shifts[i][1]
            direction = shifts[i][2]
            for j in range(start,end+1):
                if direction==1:
                    hashtable[j]+=1
                else:
                    hashtable[j]-=1
        print(hashtable)
        li = list(s)
        for ind,val in hashtable.items():
            char = li[ind]
            asci = ord(char)
            val = int(math.fmod(val,26))
            if asci+val>122:
                real = abs(122-(asci+val-1))
                fin = 97+real
                li[ind] = chr(fin)
            elif asci+val<97:
                real = 97-(asci+val+1)
                fin = 122-real
                li[ind] = chr(fin)
            else:
                li[ind] = chr(asci+val)         
        new = ''.join(li)
        return new'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for i in range(len(shifts)):
            start = shifts[i][0]
            end = shifts[i][1]
            direction = shifts[i][2]
            if direction ==1:
                prefix[start] -= 1
                prefix[end+1] += 1
            else:
                #print(prefix[start],prefix[end+1])
                prefix[start]+=1
                prefix[end+1]-=1
        print(prefix)
        li = list(s)
        diff = 0
        for i in range(len(li),-1,-1):
            diff+=prefix[i]
            #print(diff)
            char = li[i-1]
            #print(char)
            val = (ord(char) - ord('a') + diff)%26
            new = chr(val+ord('a'))
            #print(new)
            li[i-1] = new
        return ''.join(li)