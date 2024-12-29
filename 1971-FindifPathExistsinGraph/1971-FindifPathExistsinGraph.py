class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = {}
        for i in range(n):
            dic[i] = [i]
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        queue = [dic[source]]
        visited = set()
        while queue:
            temp = queue.pop(0)
            for t in temp:
                if t in visited:
                    continue
                visited.add(t)
                queue.append(dic[t])
                if t == destination:
                    return True
        return False 

        