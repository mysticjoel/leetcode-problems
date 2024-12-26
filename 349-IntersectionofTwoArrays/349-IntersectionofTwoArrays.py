class Solution:
    def intersection(self, num1: List[int], num2: List[int]) -> List[int]:
        n1=set(num1)
        n2=set(num2)
        d = {}
        for i in n1:
            d[i] = 1
        res = []
        print(d)
        for i in n2:
            if i in d:
                res.append(i)
        return res