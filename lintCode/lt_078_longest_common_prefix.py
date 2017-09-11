class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        nums = len(strs)
        if not nums:
            return ""
        for i in range(len(strs[0])):
            for j in range(1, nums):
                if len(strs[j]) == i or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
