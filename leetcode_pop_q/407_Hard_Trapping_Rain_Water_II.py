"""
Hard 407. Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""




class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not list: return 0
        ## add fringe to heap
        rows = len(heightMap)
        cols = len(heightMap[0])
        heap = []
        visited = [[False for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i in [0, rows-1] or j in [0, cols-1]:
                    heap.append((heightMap[i][j], i, j)) # format (height, i, j)
                    visited[i][j] = True #once added to heap, consider it's visited
        heapq.heapify(heap) #min-heapify
        
        ## always start from lowest value, use max_height to keep track of max so far
        ## for each current location, add adjacent locations to heap
        ## keep track of 0. heap, 1. visited, 2. max_val, 3. depth (max_height - location_height)
        
        depth = 0
        max_val = float("-inf")
        while heap:

            cur_val, cur_i, cur_j = heapq.heappop(heap)

            # update max_val if it changes
            if cur_val > max_val:
                max_val = cur_val
            for nb_i, nb_j in ((cur_i-1, cur_j), (cur_i+1, cur_j), (cur_i, cur_j-1), (cur_i, cur_j+1)):
                ## skip if visited
                if 0 <= nb_i < rows and 0<= nb_j < cols and not visited[nb_i][nb_j]:
                    nb_val = heightMap[nb_i][nb_j]                  
                    depth += max(0, max_val - nb_val)
                    visited[nb_i][nb_j] = True
                    heapq.heappush(heap,(nb_val, nb_i, nb_j))

        return depth


"""
the process is:
1. start by adding outer circle to heap
2. heappop (get lowest), assign it to max_val
3. while heappop'ed value isn't increased, keep max_val unchanged
4. add neighbors to heap
5. everytime adding an item to heap, check if it's "visited"
6. if not, continue adding and add it to "visited"
7. if neighbor item val < max_val, add water amount (max_val - nb_val)
8. increase max_val by max(max_val, cur_val)
"""

# class Solution:
#     def trapRainWater(self, heightMap: List[List[int]]) -> int:
#         if not list: return 0
#         ## add fringe to heap
#         rows = len(heightMap)
#         cols = len(heightMap[0])
#         heap = []
#         for i in range(rows):
#             for j in range(cols):
#                 if i in [0, rows-1] or j in [0, cols-1]:
#                     heap.append((heightMap[i][j], i, j)) # format (height, i, j)
#         heapq.heapify(heap) #min-heapify
        
#         ## always start from lowest value, use max_height to keep track of max so far
#         ## for each current location, add adjacent locations to heap
#         ## keep track of 0. heap, 1. visited, 2. max_val, 3. depth (max_height - location_height)
#         visited = [[False for i in range(cols)] for j in range(rows)]
#         depth = 0
#         max_val = float("-inf")
#         while heap:

#             cur_val, cur_i, cur_j = heapq.heappop(heap)

#             # update max_val if it changes
#             if cur_val > max_val:
#                 max_val = cur_val
#             for nb_i, nb_j in ((cur_i-1, cur_j), (cur_i+1, cur_j), (cur_i, cur_j-1), (cur_i, cur_j+1)):
#                 ## skip if visited
#                 if not (0 <= nb_i < rows and 0<= nb_j < cols): continue
#                 if visited[nb_i][nb_j]:  continue

#                 nb_val = heightMap[nb_i][nb_j]
#                 ## if neighbor is shorter than max_val, add height diff to depth
#                 if nb_i not in [0, rows-1] and nb_j not in [0, cols-1] and nb_val < max_val:
                    
#                     depth += max_val - nb_val
#                 ## add neighbor to heap
#                 if (nb_val, nb_i, nb_j) not in heap:
#                     heapq.heappush(heap, (nb_val, nb_i, nb_j))
#                     visited[nb_i][nb_j] = True
#         return depth
    
