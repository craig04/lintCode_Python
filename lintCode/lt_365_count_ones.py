class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        count = 0
        for i in range(32):
            if num & (1 << i):
                count += 1
        return count
