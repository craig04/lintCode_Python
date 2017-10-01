class TrieNode:
    def __init__(self):
        self.last = False
        self.edge = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        node = self.root
        for c in word:
            val = ord(c) - ord('a')
            if not node.edge[val]:
                node.edge[val] = TrieNode()
            node = node.edge[val]
        node.last = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        node = self.find(word)
        return node is not None and node.last

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        return self.find(prefix) is not None

    def find(self, word):
        node = self.root
        for c in word:
            val = ord(c) - ord('a')
            if not node.edge[val]:
                return None
            node = node.edge[val]
        return node
