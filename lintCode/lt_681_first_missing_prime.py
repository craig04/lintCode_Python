class Solution:
    """
    @param: : an array of integer
    @return: the first missing prime number
    """

    def firstMissingPrime(self, nums):
        nums = set(nums)
        i = 2
        primes = []
        while True:
            for p in primes:
                if i % p == 0:
                    break
            else:
                primes.append(i)
                if i not in nums:
                    return i
            i += 1
