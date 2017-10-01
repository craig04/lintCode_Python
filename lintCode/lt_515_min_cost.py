class Solution:
    """
    @param: costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        cost = [0] * 3
        for i in xrange(len(costs)):
            c = costs[i]
            R = c[0] + min(cost[1], cost[2])
            B = c[1] + min(cost[2], cost[0])
            G = c[2] + min(cost[0], cost[1])
            cost = [R, B, G]
        return min(cost)
