class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #print('abss'.find('as'))
        #s = set(words)
        #words = list(s)
        new = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i]!=words[j] and words[j].find(words[i])!=-1:
                    #print(words[i],words[j])
                    new.append(words[i])
        return list(set(new))