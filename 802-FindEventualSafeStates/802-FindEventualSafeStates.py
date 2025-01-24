class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdeg = [0] * n
        _graph = [[] for _ in range(n)]
        
        # Construct reverse graph and calculate out-degree
        for i in range(n):
            for x in graph[i]:
                _graph[x].append(i)
                outdeg[i] += 1

        # Initialize queue with terminal nodes
        q = deque()
        for i in range(n):
            if outdeg[i] == 0:
                q.append(i)

        vis = set()
        while q:
            cur = q.popleft()
            for x in _graph[cur]:
                if x not in vis:
                    outdeg[x] -= 1
                    # Outdegree 0 means safe node
                    if outdeg[x] == 0:
                        vis.add(x)
                        q.append(x)

        # Return nodes with out-degree 0 (safe nodes)
        return [i for i in range(n) if outdeg[i] == 0]