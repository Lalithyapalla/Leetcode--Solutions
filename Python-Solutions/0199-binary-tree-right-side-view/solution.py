# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                # Pop the current node
                current = queue.popleft()
                
                # If this is the LAST node of the current level
                if i == level_size - 1:
                    # CHANGE: Use .val instead of [1]
                    result.append(current.val) 
                
                # Add children for the next level
                # CHANGE: Use .left instead of [0]
                if current.left: 
                    queue.append(current.left)
                # CHANGE: Use .right instead of [2]
                if current.right: 
                    queue.append(current.right)
                    
        return result
