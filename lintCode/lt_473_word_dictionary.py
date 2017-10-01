class TrieNode:
    def __init__(self):
        self.last = False
        self.edge = [None] * 26


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def addWord(self, word):
        node = self.root
        for c in word:
            val = ord(c) - ord('a')
            if not node.edge[val]:
                node.edge[val] = TrieNode()
            node = node.edge[val]
        node.last = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word):
        return self.__search(word, 0, self.root)

    def __search(self, word, i, root):
        if not root:
            return False
        if i == len(word):
            return root.last
        c = word[i]
        if c == '.':
            for node in root.edge:
                if self.__search(word, i + 1, node):
                    return True
            return False
        return self.__search(word, i + 1, root.edge[ord(c) - ord('a')])
