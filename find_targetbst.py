# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        #idea 1: for each entry, check if k-entry is in tree using bisect
        #idea 2: tree traversal with hashmap, so basically same as array
        #idea 3: tree is "sorted" so use two pointers but move from middle out
        s = set()
        q = [root]
        while q:
            cur = q.pop()
            if not cur: continue
            if k-cur.val in s: return True
            q.append(cur.left)
            q.append(cur.right)
            s.add(cur.val)
        return False
            
            
        
        
        