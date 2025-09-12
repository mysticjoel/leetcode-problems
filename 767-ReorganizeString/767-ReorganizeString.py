# Last updated: 9/12/2025, 2:40:52 PM
from collections import defaultdict
from collections import deque
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        hmap: dict[str, int] = defaultdict(int)
        for char in s:
            hmap[char]+=1
        maxheap = [(-freq,char) for char,freq in hmap.items()]
        heapq.heapify(maxheap)
        if((-maxheap[0][0])>(len(s)+1)//2):
            return ""
        result =[]
        pfreq,pchar = 0,''
        while maxheap:
            freq,char = heapq.heappop(maxheap)
            result.append(char)
            if pfreq<0:
                heapq.heappush(maxheap,(pfreq,pchar))
            pfreq,pchar=freq+1,char

        return "".join(result)