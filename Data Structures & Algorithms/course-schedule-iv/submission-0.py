class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        # reach[i][j] = True if i is a prerequisite of j
        reach = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            reach[u][v] = True

        # Transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        return [reach[u][v] for u, v in queries]