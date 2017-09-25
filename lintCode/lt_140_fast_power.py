class Solution:
    """
    @param: a: A 32bit integer
    @param: b: A 32bit integer
    @param: n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        base = a
        mult = 1
        while n:
            if n & 1:
                mult = mult * base % b
            n >>= 1
            base = base * base % b
        return mult % b
