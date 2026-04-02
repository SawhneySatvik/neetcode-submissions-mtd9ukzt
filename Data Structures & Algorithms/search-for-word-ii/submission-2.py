class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word
        
        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] not in node.children
            ):
                return

            char = board[r][c]
            next_node = node.children[char]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"

            dfs(r+1, c, next_node)
            dfs(r-1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result