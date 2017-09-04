class SVNRepo:
    @classmethod
    def isBadVersion(cls, id):
        return True


# Run unit tests to check whether verison `id` is a bad version
# return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.


class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        l = 1
        r = n
        while l != r:
            m = (l + r) >> 1
            if SVNRepo.isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
