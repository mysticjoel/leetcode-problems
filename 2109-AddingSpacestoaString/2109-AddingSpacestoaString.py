class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new = ''
        start=0
        for i in spaces:
            new += s[start:i]
            new+= ' '
            start=i
        new+= s[start:len(s)]
        return new