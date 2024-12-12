import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            val = max(gifts)
            ind = gifts.index(val)
            gifts[ind]= floor(sqrt(val))
        return sum(gifts)