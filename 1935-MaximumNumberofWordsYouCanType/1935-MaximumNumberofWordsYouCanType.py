# Last updated: 9/16/2025, 11:21:56 AM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = text.split(" ")
        count = 0
        flag = 0
        for word in result:
            for ch in word:
                if ch in brokenLetters:
                    flag = 1
                    break
            if(flag==0):
                count+=1
            else:
                flag = 0
        return count