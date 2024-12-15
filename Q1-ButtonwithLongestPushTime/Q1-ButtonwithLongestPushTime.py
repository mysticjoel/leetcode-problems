class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        smallest = 0
        ind = 0
        for i in range(len(events)):
            if i==0:
                smallest = events[i][1]
                ind = events[i][0]
            else:
                if events[i][1]-events[i-1][1]>smallest:
                    smallest = events[i][1]-events[i-1][1]
                    ind = events[i][0]
                elif events[i][1]-events[i-1][1]==smallest:
                    if ind>events[i][0]:
                        smallest = events[i][1]-events[i-1][1]
                        ind = events[i][0]
        return ind
     #   [[9,4],[19,5],[2,8],[3,11],[2,15]]
                
        