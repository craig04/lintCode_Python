class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        attack = [[0] * n for i in range(n)]
        board = [['.'] * n for i in range(n)]
        result = []
        self.__solve(n, 0, attack, board, result)
        return result

    def __solve(self, n, i, attack, board, result):
        if i == n:
            result.append([])
            for j in range(n):
                result[-1].append(''.join(board[j]))
            return
        for j in range(n):
            if not attack[i][j]:
                self.__place(n, attack, board, i, j, 1)
                self.__solve(n, i + 1, attack, board, result)
                self.__place(n, attack, board, i, j, -1)

    def __place(self, n, attack, board, i, j, val):
        board[i][j] = 'Q' if val == 1 else '.'
        for k in range(n):
            attack[i][k] += val
            attack[k][j] += val
        begin = max(-i, -j)
        end = min(n - i, n - j)
        for k in range(begin, end):
            attack[i + k][j + k] += val
        begin = max(-i, j + 1 - n)
        end = min(n - i, j + 1)
        for k in range(begin, end):
            attack[i + k][j - k] += val
