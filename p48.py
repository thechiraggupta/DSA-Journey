from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)       # Left
            result.append(node.val)  # Root
            inorder(node.right)      # Right

        inorder(root)
        return result