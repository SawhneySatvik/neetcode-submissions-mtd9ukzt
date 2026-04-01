# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()

            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0])) if nodes[0] != 'N' else None

        queue = deque([root]) if root else deque([])
        i = 1
        while queue:
            node = queue.popleft()

            if nodes[i] != "N":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1

            if nodes[i] != "N":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1

        return root
