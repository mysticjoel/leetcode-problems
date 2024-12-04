class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left=0
        count = 0
        for i in range(len(str2)):
            #if (str2[i] in str1) or (chr(ord(str2[i])-1) in str1):
            left = 0
            #print(str1[left])
            while(left<len(str1)):
                #print(left,len(str1)str1[left])
                if str2[i] == str1[left]:
                    count+=1
                    str1= str1[left+1:]
                    break
                elif chr(ord(str2[i])-1) == str1[left]:
                    count+=1
                    str1 = str1[left+1:]
                    break
                elif str2[i] == 'a' and str1[left] == 'z':
                    count+=1
                    str1 = str1[left+1:]
                    break
                left+=1
        print(count)
        if count==len(str2):
            return True
        else:
            return False