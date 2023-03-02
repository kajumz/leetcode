def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentval = root.val
        pval = p.val
        qval = q.val
        if pval<parentval and qval<parentval:
            return self.lowestCommonAncestor(root.left,p,q)
        elif pval>parentval and qval>parentval:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
