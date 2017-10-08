class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Cosine similarity
    """

    def cosineSimilarity(self, A, B):
        lenA = self.__vectorLen(A)
        lenB = self.__vectorLen(B)
        mult = sum(map(lambda e: reduce(lambda x, y: x * y, e), zip(A, B)))
        return mult / (lenA * lenB) if lenA and lenB else 2

    def __vectorLen(self, v):
        from math import sqrt
        return sqrt(sum(map(lambda x: x * x, v)))
