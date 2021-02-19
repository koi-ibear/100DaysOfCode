"""
Medium 743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        edges = [dict() for _ in range(n+1)]

        for i in times:

            edges[i[0]][i[1]] = i[2]
            # edges[i[1]][i[0]] = i[2]
        frontier = [(0,k)]
        heapq.heapify(frontier)
        while frontier:
            print(frontier)
            cur_time, cur_vertex = heapq.heappop(frontier)
            print(cur_time, cur_vertex)
            if cur_vertex in visited:continue
            visited.add(cur_vertex)
            nbs = edges[cur_vertex].keys()
            for nb in nbs:
                if nb in visited: continue
                in_front = 0
                for k, (i,j) in enumerate(frontier):
                    print(k, (i,j), cur_time+edges[cur_vertex][nb])
                    if j == nb:
                        in_front = 1
                        if i > cur_time+edges[cur_vertex][nb]:
                            frontier[k] = (cur_time+edges[cur_vertex][nb], j)
                if not in_front:
                    heapq.heappush(frontier, (cur_time+edges[cur_vertex][nb], nb))
            # record = cur_time+edges[cur_vertex][nb]
        if len(visited) == n:
            # return record
            return cur_time
        return -1
