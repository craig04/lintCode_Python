class Solution:
    """
    @param: n: the nth
    @return: the nth sequence
    """

    def countAndSay(self, n):
        seq = [1]
        for i in xrange(1, n):
            b, e = 0, 0
            length = len(seq)
            nextSeq = []
            while b != length:
                while e != length and seq[b] == seq[e]:
                    e += 1
                rep = []
                self.__toStr(e - b, rep)
                nextSeq.extend(rep)
                nextSeq.append(seq[b])
                b = e
            seq = nextSeq
        return ''.join(str(x) for x in seq)

    def __toStr(self, n, result):
        c = n / 10
        if c:
            self.__toStr(c, result)
        result.append(n - c * 10)
