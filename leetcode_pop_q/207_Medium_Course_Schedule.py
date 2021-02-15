"""
Medium 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
class Solution:
    # dfs
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        prer_dict = {i:[] for i in range(numCourses)}
        for [i,j] in prerequisites:
            prer_dict[i].append(j)
        
        visited = [0 for i in range(numCourses)]
        
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in prer_dict[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                


class Solution:
    # bfs
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num = 0
        pres = [set() for i in range(numCourses)] #[set(prereqs for course 0), (prereqs of c1), ...]
        courses = [[] for i in range(numCourses)]  #[[0's following courses], [1's following courses], ...]
        for [i,j] in prerequisites:
            pres[i].add(j)
            courses[j].append(i)
        
        start = [i for i in range(numCourses) if not pres[i]] # if there's no prereqs, add to start
        
        while start:
            new_start = []
            for s in start:
                num += 1 # take one class in start list
                for c in courses[s]: # courses that depends on prereq s                    
                    pres[c].remove(s) # remove prereq s from c's prereq_set "take prereq s & remove it from courses that need it"

                    if not pres[c]:
                        start.append(c) # if all prereqs are taken, c becomes a prereq & gets added to start
            start = new_start
        
        return num == numCourses
       


"""
this problem is equivalent to "find circle in the graph"

** dfs **
1. use dictionary or list's index to track course, content is prereqs
2. use visited and "staging" flag (-1), if one node is visited, stage it as -1
if finds -1 during dfs, circle exists, return False; if nothing happens, return True
and flip visited flag to 1
3. for each course, run dfs to complete circle searching



** bfs **
1. use double list: one tracks course's prereqs and one tracks courses' successors
2. add non-prereq courses to layer queue
3. while layer has content, for each element in queue, +1 to counter
4. for each course depending on it, remove this prereq from tracker set
5. check if this course has other prereqs left, if not, add it to next layer
6. alter layer with new_layer
7. repeat while loop until layer is empty
8. return equality check between counter and numCourses
"""
