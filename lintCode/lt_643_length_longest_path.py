class Solution:
    """
    @param: input: an abstract file system
    @return: return the length of the longest absolute path to file
    """

    def lengthLongestPath(self, input):
        stack = [[-1, -1]]
        longest = 0
        for name in input.split('\n'):
            tabs = 0
            folder = True
            for c in name:
                if c == '\t':
                    tabs += 1
                elif c == '.':
                    folder = False
            while stack[-1][0] >= tabs:
                stack.pop()
            length = stack[-1][1] + 1 + len(name) - tabs
            if not folder:
                longest = max(longest, length)
            stack.append([tabs, length])
        return longest
