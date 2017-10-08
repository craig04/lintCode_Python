class Solution:
    """
    @param: : a continuous stream of numbers
    @param: : a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        try:
            index = nums.index(number)
        except ValueError:
            return -1
        count = {}
        subseq = nums[:index + 1]
        for n in subseq:
            count[n] = count.setdefault(n, 0) + 1
        for n in subseq:
            if count[n] == 1:
                return n
        return -1
