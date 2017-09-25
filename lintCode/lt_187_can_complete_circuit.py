class Solution:
    """
    @param: gas: An array of integers
    @param: cost: An array of integers
    @return: An integer
    """

    def canCompleteCircuit(self, gas, cost):
        n, i = len(cost), 0
        gas += gas
        cost += cost
        while i < n:
            g, j = 0, i
            while j < i + n:
                g += gas[j] - cost[j]
                if g < 0:
                    break
                j += 1
            else:
                return i
            i = j + 1
        return -1
