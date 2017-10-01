class Solution:
    """
    @param: num1: a non-negative integers
    @param: num2: a non-negative integers
    @return: return product of num1 and num2
    """

    def multiply(self, num1, num2):
        rev1, len1 = num1[::-1], len(num1)
        rev2, len2 = num2[::-1], len(num2)
        calc = [0] * (len1 + len2)
        for j in xrange(len2):
            c, i = 0, 0
            n2 = int(rev2[j])
            while i < len1 or c:
                n1 = int(rev1[i]) if i < len1 else 0
                n = n1 * n2 + c + calc[i + j]
                calc[i + j] = n % 10
                c = n / 10
                i += 1
        last = len(calc) - 1
        while last and calc[last] == 0:
            last -= 1
        return ''.join(str(n) for n in reversed(calc[:last + 1]))
