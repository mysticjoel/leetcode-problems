# Last updated: 9/15/2025, 8:45:55 PM
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b>0:
            heapq.heappush(heap, (-b, "b"))
        if c>0:    
            heapq.heappush(heap, (-c, "c"))

        result = []

        while heap:
            count,char = heapq.heappop(heap)
            if len(result)>=2 and result[-1] == result[-2] == char:
                if not heap:
                    break
                count2,char2 = heapq.heappop(heap)
                result.append(char2)
                if count2+1<0:
                    heapq.heappush(heap,(count2+1,char2))
                heapq.heappush(heap,(count,char))
            else:
                result.append(char)
                if count+1<0:
                    heapq.heappush(heap,(count+1,char))

        return "".join(result)