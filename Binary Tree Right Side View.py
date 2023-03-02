def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        
        def dfs(root,depth):
            if not root:
                return
            if depth == len(self.ans):
                self.ans.append(root.val)
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
        dfs(root,0)
        return self.ans
