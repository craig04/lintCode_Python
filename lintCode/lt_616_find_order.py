class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    def findOrder(self, numCourses, prerequisites):
        depend = [0] * numCourses
        rebuild = {}
        for c, p in prerequisites:
            depend[c] += 1
            rebuild.setdefault(p, []).append(c)
        learn = []
        for i in xrange(numCourses):
            if not depend[i]:
                learn.append(i)
        order = []
        while learn:
            c = learn.pop()
            order.append(c)
            for n in rebuild.setdefault(c, []):
                depend[n] -= 1
                if not depend[n]:
                    learn.append(n)
        return order if len(order) == numCourses else []
