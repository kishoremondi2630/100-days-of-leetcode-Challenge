class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list and in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # Create the graph and count in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with courses that have no prerequisites
        queue = []
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        # Perform topological sort
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            
            # Decrease in-degree of neighbors
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we processed all courses, return result; otherwise, return empty array
        return result if len(result) == numCourses else []
