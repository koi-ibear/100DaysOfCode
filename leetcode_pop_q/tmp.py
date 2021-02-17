tmp
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        edges = [dict() for _ in range(n+1)]

        for i in times:

            edges[i[0]][i[1]] = i[2]
            edges[i[1]][i[0]] = i[2]
        frontier = [(0,2)]
        heapq.heapify(frontier)
        while frontier:
            cur_time, cur_vertex = frontier.pop()
            nbs = edges[cur_vertex].keys()
            for nb in nbs:
                if nb in visited: continue
                heapq.heappush(frontier, (cur_time+edges[cur_vertex][nb], nb))
                visited.add(nb)
        if len(visited) == n:
            return cur_time
        return -1
                    