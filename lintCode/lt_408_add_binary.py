class Solution:
    """
    @param: a: a number
    @param: b: a number
    @return: the result
    """

    def addBinary(self, a, b):
        diff = len(a) - len(b)
        if diff < 0:
            a = "0" * -diff + a
        elif diff > 0:
            b = "0" * diff + b
        c = ""
        f = 0
        for i in range(-1, -len(a) - 1, -1):
            f = f + int(a[i]) + int(b[i])
            c += str(f & 1)
            f >>= 1
        if f:
            c += "1"
        return c[::-1]
