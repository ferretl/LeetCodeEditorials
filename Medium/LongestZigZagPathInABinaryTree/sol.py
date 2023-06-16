from typing import *
# this code is supplied for us :3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
            self.length = 0
            def DFS(node, depth, goRight):
                self.length = max(self.length, depth)
                if node:
                    if goRight:
                        DFS(node.right, depth + 1, False)
                        DFS(node.left, 0, True)
                    else:
                        DFS(node.left, depth + 1, True)
                        DFS(node.right, 0, False)
            DFS(root.left,0,True)
            DFS(root.right,0,False)
            return self.length