class Solution:
    """
    @param: n: a number
    @return: Gray code
    """

    def grayCode(self, n):
        codes = [0]
        for i in range(n):
            bit = 1 << i
            for t in reversed(codes):
                codes.append(t | bit)
        return codes
