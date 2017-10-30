class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """

    def addDigits(self, num):
        res = 0
        while num:
            res += num % 10
            num /= 10
        return res if res < 10 else self.addDigits(res)
