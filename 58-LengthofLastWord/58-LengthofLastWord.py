class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip()
        #print(new)
        li = new.split(' ')
        return len(li[-1])