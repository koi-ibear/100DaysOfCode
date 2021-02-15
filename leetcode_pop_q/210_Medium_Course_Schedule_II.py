"""
Medium 210. Course Schedule II


There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        dfs
        """
        prereqs = [[] for _ in range(numCourses)]
        for i,j in prerequisites:
            prereqs[i].append(j)
        visited = [0 for _ in range(numCourses)]
        ans = []
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in prereqs[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            ans.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
                

        
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         """
#         bfs
#         """
#         prepost = [[] for i in range(numCourses)]
#         postpre = [set() for i in range(numCourses)]
#         for [i,j] in prerequisites:
#             prepost[j].append(i)
#             postpre[i].add(j)
#         ready = [(i, [i]) for i in range(numCourses) if not postpre[i]] # ready for no-prereq courses
#         ans = []
#         while ready:
#             ready_new = []
#             for r, plan in ready:
#                 ans += [r]
#                 for p in prepost[r]:
#                     postpre[p].remove(r)
#                     if not postpre[p]:
#                         ready_new.append((p, plan+[p]))
                
#             ready = ready_new
#         if len(ans) == numCourses:
#             return ans        
#         return []
                