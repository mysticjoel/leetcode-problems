class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        count = 0
        c = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c.append(i)
                count+=1
            if count>2:
                return False
        if count==2:
            if s1[c[0]]==s2[c[1]] and s1[c[1]]==s2[c[0]]:
                return True
            else:
                return False
        if count==1:
            return False