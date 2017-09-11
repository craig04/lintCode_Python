class Solution:
    """
    @param: A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        yes = no = 0
        for a in A:
            t = yes
            yes = max(no + a, yes)
            no = max(t, no)
        return max(yes, no)
