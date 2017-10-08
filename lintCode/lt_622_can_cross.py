class Solution:
    """
    @param: stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """

    def canCross(self, stones):
        n = len(stones)
        pos = {}
        for i in xrange(n):
            pos[stones[i]] = i
        steps = [set() for _ in xrange(n)]
        steps[0].add(0)
        for i in xrange(n):
            arrivesteps = steps[i]
            for s in arrivesteps:
                nextsteps = filter(lambda e: e > 0, [s - 1, s, s + 1])
                for nextstep in nextsteps:
                    nextpos = stones[i] + nextstep
                    nextindex = pos.get(nextpos, -1)
                    if nextindex != -1:
                        steps[nextindex].add(nextstep)
        return len(steps[-1]) != 0
