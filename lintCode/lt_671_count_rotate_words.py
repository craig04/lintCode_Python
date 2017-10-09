class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """

    def countRotateWords(self, words):
        count = 0
        groups = []
        for word in words:
            for s in groups:
                if word in s:
                    break
            else:
                s = set()
                count += 1
                for i in range(len(word)):
                    s.add(word[i:] + word[:i])
                groups.append(s)
        return len(groups)
