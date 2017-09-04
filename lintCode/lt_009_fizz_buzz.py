class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):

        result = []
        for i in range(1, n + 1):
            remain3 = i % 3 == 0
            remain5 = i % 5 == 0
            if remain3 and remain5:
                result.append("fizz buzz")
            elif remain3:
                result.append("fizz")
            elif remain5:
                result.append("buzz")
            else:
                result.append(str(i))
        return result
