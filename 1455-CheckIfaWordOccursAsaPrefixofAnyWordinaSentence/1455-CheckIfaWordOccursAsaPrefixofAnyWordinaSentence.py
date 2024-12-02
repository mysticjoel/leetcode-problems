class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent = list(sentence.split())
        lent = len(searchWord)
        for i in range(len(sent)):
            if len(sent[i])>=lent:
                if sent[i][0:lent]==searchWord:
                    return i+1
        return -1