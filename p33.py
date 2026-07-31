class Solution:
    def isSameTree(self, p, q):
        # Case 1: both are None
        if not p and not q:
            return True
        
        # Case 2: one is None
        if not p or not q:
            return False
        
        # Case 3: values must match + check subtrees
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))