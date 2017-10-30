class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        used = set()
        while n not in used:
            if n == 1:
                return True
            used.add(n)
            n = self.__sumOfPow(n)
        return False

    def __sumOfPow(self, n):
        sum = 0
        while n != 0:
            rem = n % 10
            sum += rem * rem
            n /= 10
        return sum
