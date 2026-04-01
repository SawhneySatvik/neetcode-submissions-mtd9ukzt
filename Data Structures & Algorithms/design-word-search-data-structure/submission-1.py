class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            
            c = word[i]

            if c != '.':
                if c not in node.children:
                    return False
                return dfs(node.children[c], i+1)
            
            else:
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
        
        return dfs(self.root, 0)