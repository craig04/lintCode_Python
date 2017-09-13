class Solution:
    __instance = None

    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = Solution()
        return cls.__instance
