class Solution:
    """
    @param: : a given string
    @param: : another given string
    @return: An array of missing string
    """

    def missingString(self, str1, str2):
        set2 = set(str2.split())
        return filter(lambda e: e not in set2, str1.split())
