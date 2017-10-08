class Guess:
    @staticmethod
    def guess(num):
        return 0


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        return self.__guess(1, n)

    def __guess(self, low, up):
        mid = (low + up) >> 1
        result = Guess.guess(mid)
        if result == 0:
            return mid
        if result == 1:
            return self.__guess(mid + 1, up)
        return self.__guess(low, mid - 1)
