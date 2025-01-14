class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        for i in range(len(A)):
            seta = set(A[0:i+1])
            setb = set(B[0:i+1])
            C.append(len(seta & setb))
        return C