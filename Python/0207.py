class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)

        visited_set = set()
        
        def dfs(course):
            if course in visited_set:
                return False
            
            if pre_map[course] == []:
                return True

            visited_set.add(course)
            for prerequisite in pre_map[course]:
                if not dfs(prerequisite):
                    return False

            visited_set.remove(course)
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

        
