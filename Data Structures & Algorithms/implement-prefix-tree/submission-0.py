class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
            if i == len(word) - 1:
                node.endofword = True
        
            
    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            if i == len(word) - 1 and not node.endofword:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node.children:
                return False
            node = node.children[prefix[i]]
        return True
        
        