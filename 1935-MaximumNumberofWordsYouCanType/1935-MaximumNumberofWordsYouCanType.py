# Last updated: 9/16/2025, 11:22:30 AM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c = 0
        l = text.split()
        bl = set(brokenLetters)

        for i in l:
            for j in i:
                if j in bl:
                    break
            else:
                c += 1
        
        return c