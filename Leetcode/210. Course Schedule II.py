from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]

        for p in prerequisites:
            indegree[p[0]].add(p[1])
            outdegree[p[1]].append(p[0])

        ret, start = [], [i for i in range(numCourses) if not indegree[i]]

        while start:
            newStart = []

            for i in start:
                ret.append(i)

                for j in outdegree[i]:
                    indegree[j].remove(i)

                    if not indegree[j]:
                        newStart.append(j)

            start = newStart

        return ret if len(ret) == numCourses else []
