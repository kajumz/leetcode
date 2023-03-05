class Solution(object):
    def isMatch(self,s,t):
        if not(s and t):
            return s is t
        return (s.val == t.val and 
                self.isMatch(s.left,t.left) and
                self.isMatch(s.right,t.right)) 
    def isSubtree(self, root, subRoot):
        if self.isMatch(root,subRoot): return True
        if not root: return False
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
