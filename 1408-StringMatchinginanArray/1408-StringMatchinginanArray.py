'''class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #print('abss'.find('as'))
        #s = set(words)
        #words = list(s)
        new = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[j].find(words[i])!=-1:
                    #print(words[i],words[j])
                    new.append(words[i])
        return list(set(new))'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ' '.join(words)
        new = []
        for i in words:
            if s.count(i)>1:
                new.append(i)
        return new