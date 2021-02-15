"""
Hard 815. Bus Routes

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        visited = set() #track which buses we've been on
        
        stops = {} ## create stops to keep track of buses per stop {stop:[bus1,bus2,...]}
        for i, _ in enumerate(routes):
            for j in _:
                stops[j] = stops.get(j, set())
                stops[j].add(i)

        q = [source]
        count = 0
        while q:
            count += 1
            newq = []
            for s in q:
                # if s in visited: continue
                buses = stops[s]
                for i in buses:
                    if i in visited: continue
                    r = routes[i]
                    for j in r:
                        if j == target: return count
                        if j != source: newq.append(j)
                    visited.add(i)
                # visited.add(s)
            q = newq
        return -1
                        
"""
another bfs for graph!
1. key to graph bfs problem: create two hashes to make sure search is efficient
(in this prob, it's routes = [[stops_of_bus1], [stops_of_bus2]]
and stops = {stop1: [buses_stop_here], stop2:[buses_stop_here]}
)

2. search by layer! counter += 1 every time replace layer 
and return count when goal is found

3. use visited to track visited nodes
since we only visit one bus at most once, keep track of seen buses instead of stops
"""        

# class Solution:
#     def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
#         if source == target: return 0
#         visited = [0 for _ in range(len(routes))] #track which buses we've been on
#         q = []
#         for index, bus in enumerate(routes):
#             if source in bus:
#                 # if target in bus: return 1
#                 # q.extend([(i, 1) for i in bus if i != source])
#                 for i in bus:
#                     if i == target: return 1
#                     if i != source: q.append([i, 1])
#                 visited[index] = 1
        
#         while q:
#             newq = []
#             for s, c in q:
#                 for index, bus in enumerate(routes):
#                     if not visited[index] and s in bus:
#                         # if target in bus:
#                         #     return c+1
#                         # newq.extend([(i, c+1) for i in bus if i != s])
#                         for i in bus:
#                             if i == target: return c+1
#                             if i != source: q.append([i, c+1])

#                         visited[index] = 1
#             q = newq
#         return -1
                        
        