# Last updated: 9/13/2025, 6:50:32 PM
from collections import defaultdict
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow : dict[str,int] = defaultdict(int)
        con : dict[str,int] = defaultdict(int)
        set_ = set({'a','e','i','o','u'})
        for char in s:
            if char in set_:
                vow[char]+=1
            else:
                con[char]+=1
        
        return max(vow.values(),default=0) + max(con.values(),default=0)
