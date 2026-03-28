class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree represents each required BY how many courses 
        indegree = [0] * numCourses
        # graph represents each course's required courses
        graph = [[] for _ in range(numCourses)]
        for crs, preR in prerequisites:
            indegree[preR] += 1
            graph[crs].append(preR)

        study = deque()

        # can only study the course when there's no required
        for cs in range(numCourses):
            if indegree[cs] == 0:
                study.append(cs)
        
        done = 0
        while study:
            cur = study.popleft()
            done += 1
            for nebc in graph[cur]:
                indegree[nebc] -= 1
                if indegree[nebc] == 0:
                    study.append(nebc)
        
        return done == numCourses