class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root  = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endofword = True

    def dfs(self, string, node):

        for i, c in enumerate(string):
            if c == ".":
                for child, node in node.children.items():
                    if self.dfs(string[i + 1:], node):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                node = node.children[c]
        return node.endofword
            

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)