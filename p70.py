class Solution:
    def recoverTree(self, root):
        first = None
        second = None
        prev = None

        def inorder(node):
            nonlocal first, second, prev

            if not node:
                return

            inorder(node.left)

            # Find incorrect order
            if prev and prev.val > node.val:
                if first is None:
                    first = prev

                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        # Swap the values back
        first.val, second.val = second.val, first.val