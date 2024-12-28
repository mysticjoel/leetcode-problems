class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = []
        for _ in range(n):
            adj.append([])
        print(adj)
        for i in range(n):
            if manager[i]!=-1:
                print(i,manager[i])

                adj[manager[i]].append(i)
                #print(adj)
        #print(adj)
        maxtime = 0
        queue = deque()
        queue.append([headID,informTime[headID]])
        while queue:
            for i in range(len(queue)):
                manager, time = queue.popleft()
                maxtime = max(maxtime,time)
                for n in adj[manager]:
                    queue.append([n,time+informTime[n]])
        return maxtime