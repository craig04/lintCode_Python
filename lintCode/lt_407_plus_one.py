class Solution:
    """
    @param: digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        i, c = -1, 1
        sums = list(digits)
        while True:
            sums[i] += c
            c = 0
            if sums[i] >= 10:
                c = 1
                sums[i] -= 10
            if i == -len(sums) or c == 0:
                break
            i -= 1
        if c:
            sums.insert(0, 1)
        return sums
