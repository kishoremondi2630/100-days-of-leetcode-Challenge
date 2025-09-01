from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # Build the graph and indegree array
        for prerequisite in prerequisites:
            course, prereq = prerequisite
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Initialize a queue with all nodes that have indegree 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses
