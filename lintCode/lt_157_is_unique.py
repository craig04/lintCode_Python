class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique(self, str):
        s = set()
        for c in str:
            if c in s:
                return False
            s.add(c)
        return True
