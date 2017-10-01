class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        dic = {}
        for s in strs:
            dic.setdefault(str(sorted(s)), []).append(s)
        result = []
        for k, v in dic.items():
            if len(v) > 1:
                result.extend(v)
        return result
