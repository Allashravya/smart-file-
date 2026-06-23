class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search_prefix(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]

        words = []
        self.collect_words(node, prefix, words)

        return words

    def collect_words(self, node, current, words):

        if node.is_end:
            words.append(current)

        for char, child in node.children.items():
            self.collect_words(child, current + char, words)