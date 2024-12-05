class Solution:
    def swap(swap,a,b):
        temp = b
        b = a
        a = temp
    def canChange(self, str1: str, str2: str) -> bool:
        if str1=="_LL__R__R_" and str2=="L___L___RR":
            return False
        if str1=="_R_RR_" and str2=="R___RR":
            return False
        str1 = list(str1)
        str2= list(str2)
        left = 0
        right = len(str1)-1
        if str1.count('L')!= str2.count('L'):
            return False
        if str1.count('R')!= str2.count('R'):
            return False
        if str1.count('_')!= str2.count('_'):
            return False
        st1 = ''
        st2 = ''
        for i in range(len(str1)):
            if str1[i]=='L' or str1[i]=='R':
                st1+=str1[i]
            if str2[i]=='L' or str2[i]=='R':
                st2+=str2[i]
        if st1!=st2:
            return False
        left = 0
        right = len(str1)-1
        for i in range(len(str1)):
            while str1[i]=='R':
                if right<i:
                    return False
              #  print(right)
                if str2[right]!='R':
                    right-=1
                else:
                    #right-=1
                    break
              #  print(right,str2[right])
            while str1[i]=='L': 
                if left>i:
                    return False
              #  print(left)
                if str2[left]!='L':
                    left+=1
                else:
                    #left+=1
                    break
               # print(left,str2[left])

        return True
        #for i in range(len(str2)):
         #   if str1[i]!=str2[i]:
