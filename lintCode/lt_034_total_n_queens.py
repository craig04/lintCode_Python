class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def totalNQueens(self, n):
        attack = [[0] * n for i in range(n)]
        count = 0
        result = [0]
        for j in range((n + 1) / 2):
            self.__place(n, attack, 0, j, 1)
            result[0] = 0
            self.__solve(n, 1, attack, result)
            self.__place(n, attack, 0, j, -1)
            count += result[0]
        count <<= 1
        if n & 1:
            count -= result[0]
        return count

    def __solve(self, n, i, attack, result):
        if i == n:
            result[0] += 1
            return
        for j in range(n):
            if not attack[i][j]:
                self.__place(n, attack, i, j, 1)
                self.__solve(n, i + 1, attack, result)
                self.__place(n, attack, i, j, -1)

    def __place(self, n, attack, i, j, val):
        for k in range(n):
            attack[i][k] += val
            attack[k][j] += val
        b = max(-i, -j)
        e = min(n - i, n - j)
        for k in range(b, e):
            attack[i + k][j + k] += val
        b = max(-i, j + 1 - n)
        e = min(-i + n, j + 1)
        for k in range(b, e):
            attack[i + k][j - k] += val
