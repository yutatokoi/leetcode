class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = {c:[] for c in range(numCourses)}
        for course, prerequisite in prerequisites:
            pre_req[course].append(prerequisite)

        result = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for prerequisite in pre_req[course]:
                if not dfs(prerequisite):
                    return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result                                


